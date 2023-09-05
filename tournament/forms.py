from django.forms import ModelForm
from django import forms
from .models import tournament 

class tournamentform(ModelForm):
    class Meta:
        model=tournament
        fields=['tournament_name','game','winner_prize','runner_prize','entry_fee']

        widget = {
             'tournament_name': forms.TextInput(attrs={'class': 'form-control'}),
             'game': forms.TextInput(attrs={'class': 'form-control'}),
             'winner_prize': forms.TextInput(attrs={'class': 'form-control'}),
             'runner_prize': forms.TextInput(attrs={'class': 'form-control'}),
             'entree_fee': forms.TextInput(attrs={'class': 'form-control'}),

         }

        