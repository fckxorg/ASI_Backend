from .models import Pitch, Profile, Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from .serializers import UserSerializer
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
        return JsonResponse({"status":"Ok", "message": "Tag added"})
    return JsonResponse({"status":"Error", "message": "You have to be staff to add tags"})


@login_required
def get_tags(request):
    query = Tag.objects.all()
    data = {"tags": []}
    for tag in query:
        values = vars(tag)
        del values["_state"]
        data["tags"].append(values)
    return JsonResponse(data)
