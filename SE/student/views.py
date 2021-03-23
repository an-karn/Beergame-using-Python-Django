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
			messages.success(request, 'You have registered successfully!')
			
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

			add_to_assigned_games(student, game_id)

			return redirect(reverse('game-home', args=[game_id]))

		except Student.DoesNotExist:
			messages.info(request, 'Student with the following email does not exist')

	context = {'form':form}
	return render(request, 'student/student-enter-game.html', context)


#add to assigned_games field in Student model
def add_to_assigned_games(student, game_id):
	assigned_games = []
	#add game_id to student assigned games 
	if student.assigned_games == 'None':
		student.assigned_games = ''
		student.assigned_games += game_id 
	else:
		assigned_games = student.assigned_games.split(',')
		ignore = False
		#make sure that we have no duplicate game_ids in Student model
		for game in assigned_games:
			if game == game_id:
				ignore = True
				break
		if not ignore:
			student.assigned_games += ',' + game_id
			
	student.save()

def play_game(request, pk):
	return render(request, 'student/playerscreen.html')
# def create_game(request):
# 	return HttpResponse('Create Game')