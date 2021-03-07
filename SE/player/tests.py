from django.test import TestCase
from django.db.models import Max
from .models import player, instructor

# Create your tests here.
class PlayerTestCase(TestCase):
    def setup(self) :
        #create object sample data 
        # this is a seperate database on which we test

        p1 = player.object.create(name="Hamlet", role="distributor", inventory=10, cost=7.5, demand=45)
        p2 = player.object.create(name="Horatio", role="wholesaler", inventory=5, cost=5.5, demand=45)
