from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

#from game.urls import *
from .urls import *
from game.models import *
from .forms import *


# Create your views here.
def student_registration(request):
	form = StudentGameRegistrationForm()

	if request.method == 'POST':
		form = StudentGameRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('enter-game'))
			
	context = {'form':form}
	return render(request, 'student/student-game-registration.html', context)

def enter_game(request):
	form = StudentGameEnterForm()

	if request.method == 'POST':
		form = StudentGameEnterForm(request.POST)
		email = request.POST.get('email')

		#check if student exists
		try:
			student = Student.objects.get(email=email)
			game_id = request.POST.get('game_id')
			
			return redirect(reverse('game-home', args=[game_id]))

		except Student.DoesNotExist:
			messages.info(request, 'Student with the following email does not exist')

	context = {'form':form}
	return render(request, 'student/student-enter-game.html', context)


def play_game(request, pk):
	return render(request, 'student/student-home.html')
# def create_game(request):
# 	return HttpResponse('Create Game')