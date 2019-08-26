from django.urls import path
from . import views

urlpatterns = [
    path("user/<int:id>", views.get_user, name="get_user"),
    path("tag/", views.process_tag, name="process_tag"),
    path("login/", views.auth_user, name="auth_user"),
    path("pitch/get/new/", views.get_new_pitches, name="get_new_pitches"),
    path("user/pitch/<int:id>", views.get_users_pitches, name="get_users_pitches"),
    path("pitch/<int:id>", views.get_pitch, name="get_pitch"),
    path("register/", views.register_user, name="register_user"),
    path("pitch/add/", views.add_pitch, name="add_pitch")
]
