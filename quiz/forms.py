from django import forms
from .models import FlashCarte, MetaDonneesCarte
from connaissance.models import Cours 

#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

class FlashCarteForm(forms.ModelForm):
    '''
    permets tout bonnement la création d'une flashcarte
    '''
    cours = forms.ModelChoiceField(queryset = Cours.objects.all(), label='Cours')
    class Meta:
        model = FlashCarte
        fields = '__all__'
        labels = {
            ("dos","Remplir le dos de la carte"),
            ("type_de_note","Entrez le type de note"),
            ("devant","Remplir le devant de la carte"),
            ("image_devant","Ajoutez une image au devant"),
            ("image_dos","Ajoutez une image au dos"),
            ("publique","Enregistrer votre carte publiquement")
        }
        help_texts = {
            ("dos","Écrivez la réponse que vous cherchez à mémoriser"),
            ("type_de_note","Entrez le type de votre carte pour mieux la répertorier"),
            ("devant","Écrivez le mot ou la phrase qui va vous permettre de mémoriser la réponse"),
            ("image_devant","Ajoutez une image pour mémoriser votre réponse"),
            ("image_dos","Ajoutez une image que vous voulez mémoriser"),
            ("publique","Partagez votre carte avec d'autres utilisateurs si vous le souhaitez")
        }
        error_messages = {
            ("dos","100 caractères maximum"),
            ("type_de_note","20 caractères maximum"),
            ("devant","100 caractères maximum")
        }

    def __init__(self, *args, **kwargs):
        super(FlashCarteForm, self).__init__(*args, **kwargs)

class FlashCarteFromCSV(forms.Form):
    fichier = forms.FileField()

    def clean_fichier(self):
        fichier = self.cleaned_data['fichier']
        if not fichier.name.endswith('.csv'):
            raise forms.ValidationError("Le fichier doit être au format CSV.")
        return fichier

    def import_flashcartes(self):
        fichier = self.cleaned_data['fichier']
        flashcartes = []

        try:
            decoded_file = fichier.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                flashcarte_data = {
                    'devant': row['question'],
                    'dos': row['réponse']
                }
                form = FlashCarteForm(flashcarte_data)
                if form.is_valid():
                    flashcartes.append(form.save())
                else:
                    raise forms.ValidationError("Erreur lors de la validation du formulaire.")
        except Exception as e:
            raise forms.ValidationError("Une erreur s'est produite lors de l'importation du fichier CSV.")


class MajProchaineRevue(forms.Form):
    '''
    enregistre la nouvelle revue d'une carte pour l'utilisateur
    '''
    autoevaluation_possible = forms.ChoiceField(choices=MetaDonneesCarte.facilite_reconnaissance, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(MajProchaineRevue, self).__init__(*args, **kwargs)

    def save(self):
        if self.instance:
            autoevaluation = self.cleaned_data.get('autoevaluation_possible')
            self.instance.maj_prochaine_revue(autoevaluation)
            self.instance.save()