from django.urls import path
from . import views

urlpatterns = [
    path('student-registration/', views.student_registration, name='student-registration'),
    path('enter-game/', views.enter_game, name='enter-game'),
    path('game/<str:pk>', views.play_game, name='game-home'),
    #path('create-game/', views.create_game, name='create-game'),
]