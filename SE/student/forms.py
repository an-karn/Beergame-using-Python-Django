from django.forms import ModelForm
from .models import Student
from .admin import GameEnterForm
from django import forms

class StudentGameRegistrationForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['full_name', 'instructor_name', 'email']

class StudentGameEnterForm(GameEnterForm):
	error_css_class = "error"
	class Meta:
		model = Student
		fields = ['email', 'game_id']