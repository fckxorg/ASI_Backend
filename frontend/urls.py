from django.urls import path
from frontend import views

urlpatterns = [
    path("/", views.render_page, name="render_page")
]
