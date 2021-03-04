from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("eg", views.eg, name="eg"),
    path ("<str:name>", views.greet, name="greet")
]