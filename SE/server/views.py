from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

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