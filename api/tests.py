from django.test import TestCase, RequestFactory
from .models import Profile
from django.contrib.auth.models import User
from .views import get_user, get_user_by_id
# Create your tests here.


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

