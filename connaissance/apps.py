from django.apps import AppConfig

class ConnaissanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connaissance'

'''
La webapp CONNAISSANCE permets à un utilisateur de publier un cours, ainsi que de les organiser.
Toutes les futures applications devront s'appuyer sur des connaissances pour s'exercer et les manipuler 
'''
