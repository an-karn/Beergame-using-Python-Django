from django.db import models
# from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Student(models.Model):
	full_name = models.CharField(max_length=50)
	instructor_name = models.ForeignKey('instructor.InstructorUser', null=True, on_delete=models.SET_NULL)
	email = models.EmailField(max_length=50, unique=True)
	time_registered = models.DateTimeField(auto_now_add=True)
	assigned_games = models.CharField(max_length=50, null=True, default='None')

	
	inventory = models.IntegerField(default=0)
	backorder = models.IntegerField(default=0)
	
	upstream_player = models.CharField(max_length=50, blank=True)
	downstream_player = models.CharField(max_length=50, blank=True)
	instructors = models.CharField(max_length=50, blank=True)
	
	def __str__(self):
		return self.full_name
