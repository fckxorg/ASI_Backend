from .models import Pitch, Profile, Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from .serializers import UserSerializer


@login_required
def get_user(request):
    return JsonResponse(UserSerializer.serialize(request.user))


@login_required
def get_user_by_id(request, id):
    user = User.objects.get(id=id)
    return JsonResponse(UserSerializer.serialize(user))
