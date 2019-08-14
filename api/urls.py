from django.urls import path
from . import views

urlpatterns = [
    path("user/get/", views.get_user, name="get_user"),
    path("user/get/<int:id>", views.get_user_by_id, name="get_user_by_id"),
    path("tag/add/", views.add_tag, name="add_tag"),
    path("tag/get/", views.get_tags, name="get_tags")
]
