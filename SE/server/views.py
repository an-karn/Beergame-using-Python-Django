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

# Create your views here.
# return HttpResponse("Welcome to the Beer Game!")
def index(request):
    return render(request, "server/index.html" )

def register(request, name):
    # your role is {role}.
    if request.method == "POST":
        form = playerInfoForm(request.POST)
        if (form.is_valid()):
            playerName = form.cleaned_data["playerName"]
            return HttpResponseRedirect("index.html")
        else:
            return render(request, "server/" + name , {
                "form" : form
            })

    # elif (name.endswith(".php", len(name)-4, len(name)) == True or name.endswith(".html", len(name)-5, len(name)) == True):
        return render(request, "server/" + name, {
            "form" : playerInfoForm()
        })

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