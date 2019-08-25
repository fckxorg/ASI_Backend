from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=1500)
    is_investor = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    birth_date = models.DateField(blank=True, null=True)
    education = models.CharField(max_length=600, blank=True, null=True)
    residence = models.CharField(max_length=400, blank=True, null=True)
    bio = models.CharField(max_length=1500, blank=True, null=True)
    profiles = models.CharField(max_length=200, blank=True, null=True)  # social networks, messengers, etc.


class Pitch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=200)
    preview = models.CharField(max_length=1000)
    description = models.CharField(max_length=1500)
    video = models.CharField(max_length=1000)
    presentation = models.CharField(max_length=1000)
    necessary_investitions = models.IntegerField()  # Estimated amount of money needed for project launch
    investors_interested = models.ManyToManyField(User, related_name="investors_interested")
    investors_signed = models.ManyToManyField(User, related_name="investors_signed")
    smartid = models.CharField(max_length=400)

    def __str__(self):
        return self.name
