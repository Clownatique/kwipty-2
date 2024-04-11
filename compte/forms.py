from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Eleve
from quiz.models import PaquetCartes
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.utils import timezone

class CreationEleveForms(UserCreationForm):
    class Meta:
        model = Eleve
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom', 'email')

class ChangeEleveForms(UserChangeForm):
    class Meta:
        model = Eleve
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom', 'email')

    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        if commit:
            utilisateur.save()
        return utilisateur

class LoginForm(AuthenticationForm):
    pass
