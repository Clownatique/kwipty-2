from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreationEleveForms, ChangeEleveForms
from .models import Eleve

class EleveAdmin(admin.ModelAdmin):
    # Liste des champs à afficher
    list_display = ('username', 'email', 'nom', 'prenom', 'get_groups')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

admin.site.register(Eleve, EleveAdmin)