from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Here you can changne forms.Form to forms.ModelForm as a database is being use to store the information
class playerInfoForm(forms.Form):
    playerName = forms.CharField(label = "playerName")
    email = forms.EmailField(label = "email", max_length = 254)
    username = forms.CharField(label = "username", min_length=4, max_length=15)
    password = forms.CharField(label="password" ,min_length=8, max_length=15, widget=forms.PasswordInput)
    instructor = forms.BooleanField(label="Instructor")

# Create your views here.
# return HttpResponse("Welcome to the Beer Game!")
def index(request):
    return render(request, "server/index.html" )

def register(request):
    # your role is {role}.
    if request.method == "POST":
        form = playerInfoForm(request.POST)
        if (form.is_valid()):
            playerName = form.cleaned_data["playerName"]
            return HttpResponseRedirect('/')
        else:
            return render(request, "server/registration.html" , {
                "form" : form
            })

    def is_instructor():
        if playerInfoForm.instructor == True:
            return True
        else:
            return False
    
    return render(request, "server/registration.html", {
        "form" : playerInfoForm()
    })

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

def login(request):
    return render(request, "player/player_index.html")