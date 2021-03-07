from django.db import models

# Create your models here.
# these are python class that stores information about every er table
class player(models.Model):
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=15)
    demand = models.Integer()
    cost = models.Integer()
    inventory = models.Integer()

# Now after this class we can create functions to change a certain value
# This is done in the player.py file in the main repository

