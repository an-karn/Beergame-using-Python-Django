from django.shortcuts import render
from django import forms

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