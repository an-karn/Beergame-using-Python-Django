from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "player/player_index.html")

# <!-- length of the game , Player required => radio multiple, information sharing, 
#                     information delay, holding cost backlog cost 
#                 <input type="text" value="game_name" name="Game Name">
#                 <br\>
#                 <input type="week" value="session_length" name="Length of game"> -->

def logged_in(request):
    return render(request, "player/logged_in.html")

    def is_logged_in():
        if render(request, "player/logged_in.html") == True:
            return True
        else:
            return False

class GameCreationForm(forms.Form):
    game_name = forms.CharField(label = "Game Name")
    session_length = forms.IntegerField(label = "Length of Game", min_value=0)
    # players_present = forms.MultipleChoiceField(
    #     queryset = queryset_of_valid_choices, # not optional, use .all() if unsure
    #     widget  = forms.CheckboxSelectMultiple,) #Here we have to 
                            # add the check list with options Distributor and Wholesaler
                            # <input type="checkbox" value="{{item.id}}" name="choices">
    # max_value=int(session_length/2)
    info_sharing = forms.BooleanField(label="Information sharing allowed")
    info_delay = forms.IntegerField(label="Information Delay", min_value=0)
    starting_inventory = forms.IntegerField(label="Inventory Game starts with", min_value=0)
    holding_cost = forms.IntegerField(label="Holding Cost", min_value=0)
    backlog_cost = forms.IntegerField(label="Backlog Cost", min_value=0)

def create(request):
    if request.method == "POST":
        form = GameCreationForm(request.POST)
        if (form.is_valid()):
            return HttpResponseRedirect('/')
        else:
            return render(request, "server/create.html" , {
                "form" : form
            })

    return render(request, "server/create.html", {
            "form" : GameCreationForm()
    })