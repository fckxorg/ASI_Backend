from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Pitch)
admin.site.register(Tag)

