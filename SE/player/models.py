from django.db import models

# Create your models here.
# these are python class that stores information about every er table
class player(models.Model):
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=15)
    demand = models.Integer()
    cost = models.Integer()
    inventory = models.Integer()

    def is_valid(self):
        return self.role != None or self.cost > 0 or self.inventory >= 0

# Now after this class we can create functions to change a certain value
# This is done in the player.py file in the main repository

# class instructor(models.Model):
#     name = models.CharField(max_length=64)
#     email = models.EmailField()

    # def is_valid(self):