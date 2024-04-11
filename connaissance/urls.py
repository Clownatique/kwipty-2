from django.urls import path
from . import views

urlpatterns = [
    path("nouveau-cours/", views.creer_cours, name="creer-cours"),
    path("modifier-cours/", views.modifier_cours, name="modifier-cours"),
    path("liste-cours/", views.liste_cours, name="liste-cours"),
    path("contenu/<str:idcours>/", views.affichage_cours, name="cours"),
]
