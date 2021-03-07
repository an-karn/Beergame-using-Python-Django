from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path ("registration.html", views.register, name="register"),
    path ("create.html", views.create, name="create")
]