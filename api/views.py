from .models import Pitch, Profile, Tag
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from .serializers import UserSerializer
import base64
import json


@login_required
def get_user(request):
    return JsonResponse(UserSerializer.serialize(request.user))


@login_required
def get_user_by_id(request, id):
    user = User.objects.get(id=id)
    return JsonResponse(UserSerializer.serialize(user))


@login_required
def add_tag(request):
    if request.user.is_staff:
        data = json.loads(request.body.decode("utf-8"))
        tag = Tag(**data)
        tag.save()
        return JsonResponse({"status": "Ok", "message": "Tag added"})
    return JsonResponse({"status": "Error", "message": "You have to be staff to add tags"})


@login_required
def get_tags(request):
    query = Tag.objects.all()
    data = {"tags": []}
    for tag in query:
        values = vars(tag)
        del values["_state"]
        data["tags"].append(values)
    return JsonResponse(data)


@csrf_exempt
def auth_user(request):
    data = json.loads(request.body.decode("utf-8"))
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        response = JsonResponse({"status": "Ok", "message": "successful login"})
    else:
        response = JsonResponse({"status": "Error", "message": "Credentials are incorrect or user does not exist"})
    return response


@login_required
def get_new_pitches(request):
    if request.user.profile.is_investor:
        pitch_objects = []
        for tag in request.user.profile.tags.all():
            for element in list(tag.pitch_set.all()):
                pitch_objects.append(element)
        pitch_objects = list(set(pitch_objects))
        data = {"pitches": []}
        for pitch_object in pitch_objects:
            pitch_data = {"name": pitch_object.name, "description": pitch_object.description,
                          "preview": str(base64.b64encode(pitch_object.preview.read()))[2:-1], "tags": []}
            for tag in pitch_object.tags.all():
                pitch_data["tags"].append(tag.name)
            data["pitches"].append(pitch_data)
        return JsonResponse(data)
    return JsonResponse({"status": "Error", "message": "You have to be investor to get recommended pitches"})
