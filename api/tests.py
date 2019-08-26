from django.test import TestCase, RequestFactory, Client
from .models import Profile, Tag, Pitch
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import get_user, process_tag, get_new_pitches, get_users_pitches, get_pitch
import json


class TagTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="Test", email="test@test.com")
        self.user.set_password("/dev/null")
        self.user.save()
        self.superuser = User.objects.create(username="Sas", email="sas@test.com", password="test", is_staff=True)
        self.superuser.save()

    def test_processing_tags(self):
        data = {"name": "tech"}
        request = self.factory.post("/tag/", data, content_type="application/json")
        for user in [self.user, self.superuser]:
            request.user = user
            response = process_tag(request)
            data = json.loads(str(response.content)[2:-1])
            self.assertEqual(response.status_code, 200)
            if user.is_staff:
                self.assertEqual(data["status"], "Ok")
            else:
                self.assertEqual(data["status"], "Error")


class UserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create(username="Test", email="test@test.com")
        self.user.set_password("/dev/null")
        self.user.save()
        self.profile = Profile(user=self.user, birth_date="2019-06-09", is_investor=True,
                               avatar=SimpleUploadedFile("picture0.png", bytes("testdata", encoding='utf-8')))
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

    def test_getting_user_by_id(self):
        for case in [self.user.id, 0]:
            request = self.factory.get("/user/" + str(case))
            request.user = self.user
            response = get_user(request, self.user.id)
            self.assertEqual(response.status_code, 200)
            data = json.loads(str(response.content)[2:-1])
            self.assertEqual(data["id"], self.user.id)


    def test_logging_in(self):
        data = {"username": "Test", "password": "/dev/null"}
        response = self.client.post("/user/login/", data, content_type="application/json")
        data = json.loads(str(response.content)[2:-1])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Ok")

    def test_getting_users_pitches_by_id(self):
        for case in [self.user.id, 0]:
            request = self.factory.get("/user/pitch/" + str(case))
            request.user = self.user
            response = get_users_pitches(request, self.user.id)
            self.assertEqual(response.status_code, 200)

    def test_registering_user(self):
        data = {"username": "Sas", "password": "/dev/null", "email": "a@a.a"}
        response = self.client.post("/user/register/", data, content_type="application/json")
        response_data = json.loads(str(response.content)[2:-1])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["status"], "Ok")
        user = User.objects.get(username="Sas")
        self.assertNotEqual(user.password, data["password"])
        self.assertIsInstance(user.profile, Profile)


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

        pitch = Pitch(user=self.user, name="test", necessary_investitions=100,
                      preview=SimpleUploadedFile("picture0.png", bytes("testdata", encoding='utf-8')))
        pitch.save()
        pitch.tags.add(tag)
        pitch.investors_interested.add(self.investor)
        pitch.investors_signed.add(self.investor)
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

    def test_getting_pitch(self):
        request = self.factory.get("/pitch/1/")
        request.user = self.user
        response = get_pitch(request, 1)
        self.assertEqual(response.status_code, 200)
        data = json.loads(str(response.content)[2:-1])
