from django import forms
from .models import *
from django.contrib.auth.models import User

class JourneeFormulaire(forms.ModelForm):
    class Meta:
        model = Journee
        exclude=['jour']

class OublieFormulaire(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur",required=False)
    class Meta:
        model = User
        fields = ('email',)


        
class voirParent(forms.ModelForm):
    p1 = forms.CharField(label="Nouveau mot de passe",required=False)
    p2 = forms.CharField(label="Retaper nouveau mot de passe",required=False)
    yourpass = forms.CharField(label="Tapez votre mot de passe (uniquement si vous souhaitez changer votre mot de passe). Vous serez déconnecté si le mot de passe a bien été modifié", widget=forms.PasswordInput,required=False)
    #Photo = forms.FileField(required=False)
    class Meta:
        model = Parent
        fields = ('Prenom','Nom','Email','Numero_Telephone','Immatriculation','Couleur_voiture','Nombre_place')


class EcoleFormulaire2(forms.ModelForm):
    class Meta:
        model=Lieu
        fields = ('Nom','Adresse','Code_postal','Numero_rue','Ville')
        
class EcoleFormulaire(forms.ModelForm):
    Ecole = forms.ModelChoiceField(queryset=Ecole.objects.all())
    #C = forms.BooleanField(label = 'Cochez pour ajouter une nouvelle école')
    class Meta:
        model=Ecole
        fields=()

class AdresseFormulaire(forms.ModelForm):
    Lieu = forms.ModelChoiceField(label='Adresse par défaut',queryset = Lieu.objects.all())
    class Meta:
        model=Lieu
        fields=()
        
class ParentFormulaire(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

class LieuFormulaire(forms.ModelForm):
    class Meta:
        model = Lieu
        fields=('Nom','Adresse','Code_postal','Ville')

class VoirEnfant(forms.ModelForm):
    p1 = forms.CharField(label="Mot de passe",required=False)
    p2 = forms.CharField(label="Retaper nouveau mot de passe",required=False)
    yourpass = forms.CharField(label="Tapez votre mot de passe (uniquement si vous souhaitez changer votre mot de passe). Vous serez déconnecté si le mot de passe a bien été modifié", widget=forms.PasswordInput,required=False)
    Ecole = forms
    class Meta:
        model = User
        fields = ('first_name','last_name',)

        
class EnfantFormulaire(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password')

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class DisponibiliteFormulaire(forms.ModelForm):
  #  retour = forms.BooleanField(label = 'Cochez si départ = arrivée')
    class Meta:
        model = Disponibilite
        fields = ('debut','fin','jour','LieuCollecte')
