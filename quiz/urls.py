from django.urls import path
from . import views

urlpatterns = [
    path("cartes/<str:metadonnes_carte_id>", views.reviser_carte, name="reviser-carte"),
    path("cartes/revision/", views.reviser_cartes_ajourdhui, name='reviser-cartes'),
    path("cartes/creer-carte/", views.creer_une_carte, name='creer-carte'),
    path("cartes/creer-cartes/", views.creer_des_cartes, name='creer-cartes'),
    path("cartes/liste/", views.voir_cartes, name="voir-cartes-disponibles"),
    path("cartes/liste/ajout/<int:carteid>", views.ajouter_carte, name="ajout-carte"),
    path("cartes/deck/", views.voir_deck, name="voir-deck"),
    path("cartes/deck/<int:carteid>/modifier/", views.ajouter_carte, name="ajout-carte"),
    path("cartes/deck/<int:metadonnesid>/supprimer/", views.supprimer_carte, name="supprimer-carte"),
    path("cartes/deck/<int:carteid>/parametre", views.ajouter_carte, name="parametre-carte"),
]
