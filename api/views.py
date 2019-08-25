from .models import Pitch, Profile, Tag
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from .serializers import UserSerializer
import pickle
import json

from django.core.serializers import serialize


@csrf_exempt
def add_pitch(request):
    user = User.objects.get(email="max.kokryashkin@gmail.com")
    data = json.loads(request.body.decode("utf-8"))
    pitch = Pitch(**data)
    pitch.user = user
    pitch.save()
    pitch.tags.add(Tag.objects.get(name="design"))
    pitch.save()
    response = JsonResponse({"status": "Ok"})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET"
    return response


def get_user(request):
    user = User.objects.get(email="max.kokryashkin@gmail.com")
    response = JsonResponse(UserSerializer.serialize(user))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET"
    return response


def get_user_by_id(request, id):
    user = User.objects.get(id=id)
    return JsonResponse(UserSerializer.serialize(user))


@csrf_exempt
def add_tag(request):
    if request.user.is_staff:
        data = json.loads(request.body.decode("utf-8"))
        tag = Tag(**data)
        tag.save()
        return JsonResponse({"status": "Ok", "message": "Tag added"})
    return JsonResponse({"status": "Error", "message": "You have to be staff to add tags"})


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
    user = authenticate(request, **data)
    if user is not None:
        login(request, user)
        response = JsonResponse({"status": "Ok", "message": "successful login"})
    else:
        response = JsonResponse({"status": "Error", "message": "Credentials are incorrect or user does not exist"})
    response["Access-Control-Allow-Origin"] = "http://192.168.43.119:8000/"
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Credentials"] = True
    return response


@csrf_exempt
def get_new_pitches(request):
    pitch_objects = []
    user = User.objects.get(email="max.kokryashkin@gmail.com")
    for tag in user.profile.tags.all():
        for element in list(tag.pitch_set.all()):
            pitch_objects.append(element)
    pitch_objects = list(set(pitch_objects))
    pitch_objects = json.loads(serialize("json", pitch_objects, fields = ["name", "description", "preview", "tags"]))
    data = []
    for pitch_object in pitch_objects:
        data.append({**pitch_object["fields"], "id": pitch_object["pk"]})
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET"
    return response


def get_users_pitches(request):
    user = User.objects.get(email="max.kokryashkin@gmail.com")
    pitches = Pitch.objects.all().filter(user=user)
    data = []
    pitch_objects = json.loads(serialize("json", pitches, fields=["name", "description", "preview", "tags"]))
    for pitch_object in pitch_objects:
        data.append({**pitch_object["fields"], "id": pitch_object["pk"]})
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET"
    return response


def get_users_pitches_by_id(request, id):
    user = User.objects.get(id=id)
    pitches = Pitch.objects.all().filter(user=user)
    data = {"pitches": []}
    pitch_objects = json.loads(serialize("json", pitches, fields=["name", "description", "preview", "tags"]))
    for pitch_object in pitch_objects:
        data["pitches"].append({**pitch_object["fields"], "id": pitch_object["pk"]})
    return JsonResponse(data)


def get_pitch_by_id(request, id):
    pitch = Pitch.objects.get(id=id)
    data = json.loads(serialize('json', [pitch]))[0]
    response = JsonResponse({**data["fields"], "id": data["pk"]}, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET"
    return response


@csrf_exempt
def register_user(request):
    data = json.loads(request.body.decode("utf-8"))
    user = User.objects.create_user(**data)
    user.save()
    profile = Profile(user=user, is_investor=False)
    profile.save()
    return JsonResponse({"status": "Ok"})

@csrf_exempt
def edit_user(request):
    data = json.loads(request.body.decode("utf-8"))
    user = request.user
