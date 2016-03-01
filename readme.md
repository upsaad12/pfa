parent ne peut se modifier.
Mettre champ edt enfant ville non obligatoire (pas rammené)
class Covoiturage
    h_depart = models.TimeField
    h_arrivee = models.TimeField
    conducteur = models.ForeignKey(Parent)
    

class Passager
    covoit = models.ForeignKey(Covoiturage)
    enf = models.ForeignKey(Enfant)
    
class Enfant
    userE = models.ForeignKey(User)
    EDT = models.ForeignKey(Edt)
    parent = models.ForeignKey(Parent)
    Ecole = models.ForeignKey(Ecole)


class Parent
    Immatriculation = models.CharField
    Couleur_voiture = models.CharField
    Nombre_place = models.CharField


class Journee
    jour = models.CharField
    Matin = models.TimeField
    Soir = models.TimeField
    LieuM = models.ForeignKey(Lieu)
    LieuS = models.ForeignKey(Lieu)

class Disponibilite
    jour = models.CharField
    debut = models.TimeField
    fin = models.TimeField
    Lieu = models.ForeignKey(Lieu)
    userP = models.ForeignKey(Parent)

class Ecole
    Adresse = models.ForeignKey(Lieu)


class Edt
     L = models.ForeignKey(Journee)
     M = models.ForeignKey(Journee)
     Mer = models.ForeignKey(Journee)
     J = models.ForeignKey(Journee)
     V = models.ForeignKey(Journee)
     S = models.ForeignKey(Journee)

Jour J, heure H:
     parent:
	Dispo.UserP=parent
	Dispo.jour=J
	Dispo.debut < H < Dispo.fin ?

     enfant:
	Enfant.EDT.{L/.../S}.jour=J
	Enfant.EDT.{L/.../S}.matin / .soir	

     
class cov:
      Jour    : L ... S
      User    : id user
      HoraireDepart  : 
      HoraireArrivee  : (apres calculs via googlemaps)
      LieuDepart     : adresse enfant si matin, ecole si soir
      		       lieu adulte ?
      LieuArrivee     : addresse ecole si matin, enfant si soir
      		       lieu adulte ?

		       besoin booléen pour savoir si parent LieuD=LieuA
      parent : DispoDebut < HD < HA < DispoFin


def cov(Usera,joura,HD,HA,LD,LA):
HA et LA peuvent être False
Usera = id user