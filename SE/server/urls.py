from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path ("registration.php", views.register, name="register"),
    path ("create.html", views.create, name="create")
]