from django.test import TestCase, RequestFactory
from .models import Profile, Tag
from django.contrib.auth.models import User
from .views import get_user, get_user_by_id, add_tag, get_tags
import json


class TagTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="Test", email="test@test.com", password="test")
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
        self.user = User.objects.create(username="Test", email="test@test.com", password="test")
        self.user.save()
        self.profile = Profile(user=self.user, birth_date="2019-06-09", is_investor=True)
        self.profile.save()

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

