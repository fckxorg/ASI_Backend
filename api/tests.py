from django.test import TestCase, RequestFactory, Client
from .models import Profile, Tag, Pitch
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import get_user, get_user_by_id, add_tag, get_tags, get_new_pitches, get_users_pitches
import json


class TagTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="Test", email="test@test.com")
        self.user.set_password("/dev/null")
        self.user.save()
        self.superuser = User.objects.create(username="Sas", email="sas@test.com", password="test", is_staff=True)
        self.superuser.save()

    def test_adding_tag_as_staff(self):
        data = {"name": "tech"}
        request = self.factory.post("/tag/add", data, content_type="application/json")
        request.user = self.superuser
        response = add_tag(request)
        data = json.loads(str(response.content)[2:-1])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Ok")

    def test_adding_tag_as_base_user(self):
        data = {"name": "tech"}
        request = self.factory.post("/tag/add", data, content_type="application/json")
        request.user = self.user
        response = add_tag(request)
        data = json.loads(str(response.content)[2:-1])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Error")

    def test_getting_tags(self):
        tag = Tag(name="tech")
        tag.save()
        tag = Tag(name="art")
        tag.save()
        request = self.factory.get("/tag/get")
        request.user = self.user
        response = get_tags(request)
        self.assertEqual(response.status_code, 200)


class UserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create(username="Test", email="test@test.com")
        self.user.set_password("/dev/null")
        self.user.save()
        self.profile = Profile(user=self.user, birth_date="2019-06-09", is_investor=True)
        self.profile.save()

        tag = Tag(name="art")
        tag.save()

        pitch = Pitch(user=self.user, name="test", necessary_investitions=100,
                      preview=SimpleUploadedFile("picture0.png", bytes("testdata", encoding='utf-8')))
        pitch.save()
        pitch.tags.add(tag)
        pitch.save()

        pitch = Pitch(user=self.user, name="sas", necessary_investitions=100,
                      preview=SimpleUploadedFile("picture1.png", bytes("testdata", encoding='utf-8')))
        pitch.save()
        pitch.tags.add(tag)
        pitch.save()

    def test_getting_user(self):
        request = self.factory.get("/user/get")
        request.user = self.user
        response = get_user(request)
        self.assertEqual(response.status_code, 200)

    def test_getting_user_by_id(self):
        request = self.factory.get("/user/get/"+str(self.user.id))
        request.user = self.user
        response = get_user_by_id(request, self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_logging_in(self):
        data = {"username": "Test", "password": "/dev/null"}
        response = self.client.post("/user/login/", data, content_type="application/json")
        data = json.loads(str(response.content)[2:-1])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Ok")

    def test_getting_users_pitches(self):
        request = self.factory.get("/user/pitch/")
        request.user = self.user
        response = get_users_pitches(request)
        self.assertEqual(response.status_code, 200)


class PitchTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        tag = Tag(name="art")
        tag.save()
        tag2 = Tag(name="tech")
        tag2.save()
        self.user = User.objects.create(username="Test", email="test@test.com")
        self.user.set_password("/dev/null")
        self.user.save()
        profile = Profile(user=self.user, birth_date="2019-06-09", is_investor=False)
        profile.save()

        self.investor = User.objects.create(username="Investor", email="investor@test.com")
        self.investor.set_password("/dev/null")
        self.investor.save()
        investor_profile = Profile(user=self.investor, birth_date="2019-06-09", is_investor=True)
        investor_profile.save()
        investor_profile.tags.add(tag)
        investor_profile.tags.add(tag2)
        investor_profile.save()

        pitch = Pitch(user=self.user, name="test", necessary_investitions=100, preview=SimpleUploadedFile("picture0.png", bytes("testdata", encoding='utf-8')))
        pitch.save()
        pitch.tags.add(tag)
        pitch.save()

        pitch = Pitch(user=self.user, name="sas", necessary_investitions=100,
                      preview=SimpleUploadedFile("picture1.png", bytes("testdata", encoding='utf-8')))
        pitch.save()
        pitch.tags.add(tag)
        pitch.tags.add(tag2)
        pitch.save()

        pitch = Pitch(user=self.user, name="kek", necessary_investitions=100,
                      preview=SimpleUploadedFile("picture2.png", bytes("testdata", encoding='utf-8')))
        pitch.save()
        pitch.tags.add(tag2)
        pitch.save()

    def test_getting_new_pitches_as_investor(self):
        request = self.factory.get("/pitch/get/new/")
        request.user = self.investor
        response = get_new_pitches(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(str(response.content)[2:-1])
        self.assertEqual(data["pitches"][0]["name"], "test")

    def test_getting_new_pitches_as_user(self):
        request = self.factory.get("/pitch/get/new/")
        request.user = self.user
        response = get_new_pitches(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(str(response.content)[2:-1])
        self.assertEqual(data["status"], "Error")
