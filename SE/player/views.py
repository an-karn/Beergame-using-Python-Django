from django.shortcuts import render
from django import forms

# Create your views here.
def index(request):
    return render(request, "player/index.html")

# <!-- length of the game , Player required => radio multiple, information sharing, 
#                     information delay, holding cost backlog cost 
#                 <input type="text" value="game_name" name="Game Name">
#                 <br\>
#                 <input type="week" value="session_length" name="Length of game"> -->

class GameCreationForm(forms.Form):
    class Meta:
        game_name = forms.CharField(label = "Game Name")
        session_length = forms.Integer(label = "Length of Game")
        players_present = forms.checklist(label = "Players Present") #Here we have to 
                            # add the check list with options Distributor and Wholesaler
        info_sharing = forms.Boolean(label="Information sharing allowed")
        info_delay = forms.Integer(label="Information Delay")
        starting_inventory = forms.Integer(label="Inventory Game starts with")
        holding_cost = forms.Interger(label="Holding Cost")
        backlog_cost = forms.Interger(label="Backlog Cost")

def create(request):
    return render(request, "server/create.html", {
            "form" : GameCreationForm()
    })