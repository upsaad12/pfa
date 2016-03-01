from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.accueil),
    url(r'^inscription/$',views.inscription),
    url(r'^ajoutEnfant/$',views.ajoutEnfant),
    url(r'^modifier/$',views.modifier),
    url(r'^adresse/$',views.adresse),
    url(r'^ajoutAdresse/$',views.ajoutAdresse),
    url(r'^connexion/$',views.connexion),
    url(r'^deconnexion/$',views.deconnexion),
    url(r'^ajoutDispo/$',views.ajoutDisponibilite),
    url(r'^dispo/$',views.disponibilite),
    url(r'^voiradresse/(?P<id>\d+)/$',views.voiradresse),
    url(r'^enfant/$',views.voirenfants),
    url(r'^enfant/(?P<ida>\d+)/$',views.voirenfant),
    url(r'^enfant/(?P<ida>\d+)/(?P<jour>[L,M,D,J,V,S])/$',views.modifierEdt),
    url(r'^enfant/(?P<ida>\d+)/des/$',views.supprimerEnfant),
    url(r'^enfant/(?P<ida>\d+)/Ecole/$',views.modifierEcole),
    url(r'^enfant/(?P<ida>\d+)/ajouterEcole/$',views.ajouterEcole),
    url(r'^(?P<ida>\d+)/des/$',views.supprimerDispo),
    url(r'^covoiturage/$',views.covoiturage),
    url(r'^oublie/$',views.oublie),
    
]
