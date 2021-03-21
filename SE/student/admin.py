from django import forms

from django.contrib import admin

from .models import Student
from game.models import Game
# Register your models here.



#admin.site.register(Student)

class GameEnterForm(forms.ModelForm):
    """A form for entering game. Includes email and game id."""
    game_id = forms.CharField(label='Game number')

    class Meta:
        model = Student
        fields = ('email',)

    #game_id validator
    def clean_game_id(self):
        # Check that game_id exists
        game_id = self.cleaned_data.get("game_id")        
        try:
            game = Game.objects.get(game_id=game_id)
        except Game.DoesNotExist:
            raise forms.ValidationError("Game number not found")

        return game_id

