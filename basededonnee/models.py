from django.db import models
from django.core.validators import RegexValidator
import os
import datetime
from django.contrib.auth.models import User, UserManager
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#from solr.thumbnail import get_thumbnail
from django.core.files import File
JOURS = (
    ('lundi', 'Lundi'),
    ('mardi', 'Mardi'),
    ('mercredi', 'Mercredi'),
    ('jeudi', 'Jeudi'),
    ('vendredi', 'Vendredi'),
    ('samedi', 'Samedi'),
)


#user : username, first_name, last_name, email, password, is_active, last_login, date_joined 
#passwd : set_password(mdp)      (faire un .save() apres)
#         check_(password(mdp)
#         set_unusable_password()    utilisateur n'a pas de mdp
#         has_usable_password()      utilisateur a mot de passe valide

class Lieu(models.Model):
    Nom = models.CharField(max_length=40, null=True)
    Adresse = models.CharField(max_length=100, null=True)
    Code_postal = models.CharField(max_length=8, null=True)
    Numero_rue = models.CharField(max_length=5, null=True)
    Ville = models.CharField(max_length=40, null=True)
    proprietaire = models.ForeignKey(User,unique=False,null=True)
    x = models.DecimalField(max_digits = 15, decimal_places = 10, null=True)
    y = models.DecimalField(max_digits = 15, decimal_places = 10, null=True)
    def __str__(self):
        return self.Nom

class Ecole(models.Model):
    Adresse = models.ForeignKey(Lieu, null=True)
    def __str__(self):
        return "%s, %s %s %s %s" % (self.Adresse.Nom, self.Adresse.Numero_rue,self.Adresse.Adresse,self.Adresse.Code_postal,self.Adresse.Ville)
    
class Parent(models.Model):
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Format de numéro de téléphone incorrect.")
    place_regex = RegexValidator(regex=r'^\d{0,3}$', message="Format de nombre de place incorrect.")
    userP = models.ForeignKey(User,unique=False)
    Prenom = models.CharField(max_length=30, null=True)
    Nom = models.CharField(max_length=30, null=True)
    Email = models.EmailField(null=True)
    Numero_Telephone = models.CharField(validators=[phone_regex],max_length=15,blank=True,null=True)
    Immatriculation = models.CharField(max_length=15,blank=True,null=True)
    Couleur_voiture = models.CharField(max_length=15,blank=True,null=True)
    Nombre_place = models.CharField(null=True,blank=True,max_length=3,validators=[place_regex])
    photo = models.FileField(upload_to = '',default='Media/nope.jpg')
    Lieu = models.ForeignKey(Lieu,unique=False, null=True)
    def __str__(self):
        return self.userP.username
    def delete(self, *args, **kwargs):
        self.userP.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

class Journee(models.Model):
    jour = models.CharField(max_length=8,choices=JOURS,default='Lundi')
    Matin = models.TimeField(default=datetime.time(8,0))
    Soir = models.TimeField(default=datetime.time(17,0))
    LieuM = models.ForeignKey(Lieu,unique=False,related_name='LieuM',null=True)
    LieuS = models.ForeignKey(Lieu,unique=False,related_name='LieuS',null=True)
    def __str__(self):
        l = str(self.jour)
        return 'matin : %s - %s\n soir : %s - %s\n' %(self.LieuM,self.Matin,self.LieuS,self.Soir)

class Edt(models.Model):
     L = models.ForeignKey(Journee,related_name='L',null=True)
     M = models.ForeignKey(Journee,related_name='M',null=True)
     D = models.ForeignKey(Journee,related_name='D',null=True)
     J = models.ForeignKey(Journee,related_name='J',null=True)
     V = models.ForeignKey(Journee,related_name='V',null=True)
     S = models.ForeignKey(Journee,related_name='S',null=True)
     def __str__(self):
         return 'edt affiché ici'

class Enfant(models.Model):
    userE = models.ForeignKey(User,unique=False)
    EDT = models.ForeignKey(Edt,null=True)
    parent = models.ForeignKey(Parent,null=True,unique=False)
    Ecole = models.ForeignKey(Ecole, null=True, unique=False)
    def __str__(self):
        return self.userE.username
    def delete(self, *args, **kwargs):
        self.userE.delete()
        self.EDT.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class Disponibilite(models.Model):
    jour = models.CharField(max_length=8,choices=JOURS,null=True)
    debut = models.TimeField(null=True)
    fin = models.TimeField(null=True)
    LieuCollecte = models.ForeignKey(Lieu,null=True,unique=False)
    userP = models.ForeignKey(Parent, unique = False, null=True)
    #retour = models.NullBooleanField(null=True)
    def __str__(self):
       # if self.retour == True:
        #    return "%s %s : %s - %s retour" % (self.jour,self.Lieu,self.debut, self.fin)
        return "%s %s : %s - %s" % (self.jour,self.LieuCollecte,self.debut, self.fin)      

class Covoiturage(models.Model):
    LieuDepart = models.ForeignKey(Lieu,null=True,unique=False)
    h_depart = models.TimeField(null=True)
    h_arrivee = models.TimeField(null=True)
    conducteur = models.ForeignKey(Parent,null=True,unique=False)
    def __str__(self):
        return "%s:%s %s %s " % (self.LieuDepart,self.h_depart,self.conducteur.Immatriculation,self.conducteur.Couleur_voiture)
                                
class Passager(models.Model):
    covoit = models.ForeignKey(Covoiturage,null=True,unique=False)
    enf = models.ForeignKey(Enfant,null=True,unique=False)

class covUtil(models.Model):
    jour = models.CharField(max_length=8,choices=JOURS,null=True)
    Usr = models.ForeignKey(User,null=True,unique=False)
    horaireDepart = models.TimeField(null=True)
    horaireArrivee = models.TimeField(null=True)
    LieuDepart = models.ForeignKey(Lieu,null=True,related_name='LieuDepart')
    LieuArrivee = models.ForeignKey(Lieu,null=True,related_name='LieuArrivee')
    def __str__(self):
        return "%s %s:%s %s:%s" % (self.jour, self.horaireDepart, self.LieuDepart, self.horaireArrivee,self.LieuArrivee)
