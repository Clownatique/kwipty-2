from django.shortcuts import render, redirect, get_object_or_404
from .models import FlashCarte, MetaDonneesCarte, PaquetCartes
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import FlashCarteForm, MajProchaineRevue,FlashCarteFromCSV
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from .forms import MajProchaineRevue
from compte.models import Eleve, DeckUtilisateur
from datetime import date

def voir_cartes(request):
    cartes = FlashCarte.objects.filter(publique=True)
    context = {
        'cartes':cartes
    }
    return render(request, 'quiz/liste toutes les cartes .html', context)

def voir_deck(request):
    eleve = Eleve.objects.get(pk=request.user.id)
    deck = DeckUtilisateur.objects.get(eleve=eleve)
    cartes = MetaDonneesCarte.objects.filter(eleve=eleve)
    context = {
        'deck':deck.cartes,
        'cartes':cartes
    }
    return render(request, 'quiz/liste deck utilisateur.html', context)

def reviser_carte(request, metadonnes_carte_id):
    ''' modifier cette fonction pour qu'elle puisse prendre en argument DES cartes 
        (sous forme de queryset) OU simplement une carte (cas ou l'utilisateur veut une preview d'une carte)
    '''
    metadonnescarte = MetaDonneesCarte.objects.get(id=metadonnes_carte_id)
    if request.method == "POST":
        forme = MajProchaineRevue(request.POST)
        if forme.is_valid():
            autoevaluation_possible = forme.cleaned_data['autoevaluation_possible']
            metadonnescarte.maj_prochaine_revue(autoevaluation_possible)
            return redirect(request.META.get('HTTP_REFERER', 'menu'))
    context = {
        'carte': metadonnescarte.carte,
        'metadonnescarte': metadonnescarte,
        'forme': MajProchaineRevue(request.POST),
    }
    return render(request, 'quiz/carte.html', context)

def reviser_cartes_ajourdhui(request):
    pqt_revision = PaquetCartes.objects.create()
    cartes_a_reviser = MetaDonneesCarte.objects.filter(date_de_revue__lte=date.today(), eleve=request.user)
    for meta_carte in cartes_a_reviser:
        return reviser_carte(request, meta_carte.id)

    return redirect('menu')

def ajouter_carte(request, carteid):
    carte = FlashCarte.objects.get(id = carteid)
    eleve = Eleve.objects.get(id=request.user.id)
    temp_meta= MetaDonneesCarte.objects.create(carte=carte,
                                                eleve=eleve,
                                                date_de_revue=date.today(),
                                                phase=0)
    temp_meta.save()
    deck = DeckUtilisateur.objects.get(eleve=eleve)
    deck.cartes.add(temp_meta)
    return redirect('voir-cartes-disponibles')

def creer_des_cartes(request):
    carteforme = FlashCarteFromCSV(request.POST)
    if request.method == "POST":
        if carteforme.is_valid():
            carteforme.save()
            return redirect('voir-cartes-disponibles')
    return render(request, 'quiz/creation_flashcartes.html',{'forme': carteforme})  

def creer_une_carte(request):
    carteforme = FlashCarteForm(request.POST)
    if request.method == "POST":
        if carteforme.is_valid():
            carteforme.save()
            return redirect('voir-cartes-disponibles')
    return render(request, 'quiz/creation_flashcarte.html',{'forme': carteforme})  

def supprimer_carte(request, metadonnesid):
    deck = DeckUtilisateur.objects.get(eleve = request.user.id)
    metadonnescarte = MetaDonneesCarte.objects.get(id = metadonnesid)
    deck.cartes.remove(metadonnescarte)
    deck.save()
    return redirect('voir-deck')

def modifier_carte(request, metadonnesid):
    pass