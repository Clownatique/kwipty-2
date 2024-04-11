from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Eleve, DeckUtilisateur

@receiver(post_save, sender=Eleve)
def create_deck_utilisateur(sender, instance, created, **kwargs):
    if created:
        DeckUtilisateur.objects.create(eleve=instance)