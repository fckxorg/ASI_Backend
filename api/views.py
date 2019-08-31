"""Views module of django api app."""
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.shortcuts import decode_json, serialize_pitches
from api.status_codes import StatusCode
from api.models import Pitch, Profile, Tag


@csrf_exempt
def add_pitch(request):
    """Use this method to add pitch with provided data."""
    user = User.objects.get(email='max.kokryashkin@gmail.com')
    pitch_data = decode_json(request)
    pitch = Pitch(**pitch_data)
    pitch.u
    pitch.save()
    pitch.tags.add(Tag.objects.get(name='design'))
    pitch.save()
    return JsonResponse(StatusCode.SUCCESS)


@login_required
def get_user(request, user_id):
    """
    Use this method to get information about user.

    If passed id is zero, returns information about requesting user
    """
    if user_id == 0:
        user = request.user
    else:
        user = User.objects.get(id=user_id)

    base_fields = ['username', 'first_name', 'last_name', 'email']
    base_data = json.loads(serialize('json', [user], fields=base_fields))[0]
    profile_data = json.loads(serialize('json', [user.profile]))[0]
    full_user_information = {**base_data['fields'], **profile_data['fields']}
    full_user_information['id'] = base_data['pk']
    full_user_information.pop('user')
    return JsonResponse(full_user_information)


@login_required
def process_tag(request):
    """
    Use this method for operations with tags.

    POST: adds tag, GET: returns list of available tags
    """
    if request.method == 'POST':
        if request.user.is_staff:
            tag_information = decode_json(request)
            tag = Tag(**tag_information)
            tag.save()
            return JsonResponse({'status': 'Ok'})
        return JsonResponse(generate_response('10'))
    if request.method == 'GET':
        query = Tag.objects.all()
        raw_data = json.loads(serialize('json', query, fields=['name']))
        tags_information = {**raw_data['fields'], 'id': raw_data['pk']}
        return JsonResponse(tags_information)


@csrf_exempt
def auth_user(request):
    """Use this method for authorization."""
    auth_data = decode_json(request)
    user = authenticate(request, **auth_data)
    if user is not None:
        login(request, user)
        return JsonResponse(StatusCode.SUCCESS)
    return JsonResponse(StatusCode.ERR_AUTH)


@login_required
def get_new_pitches(request):
    """
    Use this method to get list of new pitches.

    If user not an investor returns error
    """
    if request.user.profile.is_investor:
        pitches = []
        for tag in request.user.profile.tags.all():
            for element in list(tag.pitch_set.all()):
                pitches.append(element)
        pitches = list(set(pitches))
        return JsonResponse(serialize_pitches(pitches))
    return JsonResponse(StatusCode.ERR_NOT_ALLOWED)


@login_required
def get_users_pitches(request, user_id):
    """
    Use this method to get user's pitches.

    If passed id is zero, returns pitches of user who made request.
    """
    if user_id == 0:
        user = request.user
    else:
        user = User.objects.get(id=user_id)
    pitches = Pitch.objects.all().filter(user=user)

    return JsonResponse(serialize_pitches(pitches))


@login_required
def get_pitch(request, pitch_id):
    """Use this method to get pitch information by id."""
    pitch = Pitch.objects.get(id=pitch_id)
    pitch = json.loads(serialize('json', [pitch]))[0]
    return JsonResponse({**pitch['fields'], 'id': pitch['pk']})


@csrf_exempt
def register_user(request):
    """Use this method to register user."""
    register_data = decode_json(request)
    user = User.objects.create_user(**register_data)
    user.save()
    profile = Profile(user=user, is_investor=False)
    profile.save()
    return JsonResponse(StatusCode.SUCCESS)
