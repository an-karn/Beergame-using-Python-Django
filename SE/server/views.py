from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# return HttpResponse("Welcome to the Beer Game!")
def index(request):
    return render(request, "server/index.html")

def eg(request):
    return HttpResponse("Hello you are using an example")

def greet(request, name):
    # your role is {role}.
    # return HttpResponse(f"Welocme, {name.capitalize()} to the beer game.")
    return render(request, "server/greet.html", {
        "name" : name.capitalize()
    })