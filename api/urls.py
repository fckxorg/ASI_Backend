from django.urls import path
from . import views

urlpatterns = [
    path("user/get/", views.get_user, name="get_user"),
    path("user/get/<int:id>", views.get_user_by_id, name="get_user_by_id"),
    path("tag/add/", views.add_tag, name="add_tag"),
    path("tag/get/", views.get_tags, name="get_tags"),
    path("user/login/", views.auth_user, name="auth_user"),
    path("pitch/get/new/", views.get_new_pitches, name="get_new_pitches"),
    path("user/pitch/", views.get_users_pitches, name="get_users_pitches")
]
