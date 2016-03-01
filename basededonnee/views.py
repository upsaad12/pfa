from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render,redirect
from basededonnee.forms import *
from basededonnee.models import *
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.conf import settings
import googlemaps
from django.core.mail import send_mail, EmailMessage
from django.core.files.images import get_image_dimensions
from django.utils.datastructures import MultiValueDictKeyError
import random
gmaps = googlemaps.Client(key='AIzaSyDsRQgm9WRk7PC08yphpiw7aGeyrpnNP24 ')
# subject = form.cleaned_data['subject']


def oublie(request):
    form = OublieFormulaire()
    if request.method == 'POST':
        form = OublieFormulaire(request.POST)
        if form.is_valid():
            mail = request.POST.get('email')
            usernam = request.POST.get('username')
            
            if usernam == '' and mail == '':
                return render(request, 'basededonnee/oublie.html',{'form':form,'rate':0})
            if usernam != '' and mail != '':
                usera = User.objects.filter(username=usernam, email=mail)
                if len(usera) != 1:
                    return render(request, 'basededonnee/oublie.html',{'form':form,'rate':2})
                usera = User.objects.filter(username=usernam, email=mail)[0]                    

            if usernam != '' and mail == '':
                usera = User.objects.filter(username=usernam)
                if len(usera) != 1:
                    return render(request, 'basededonnee/oublie.html',{'form':form,'rate':1})
                usera = User.objects.filter(username=usernam)[0]                
                    
            if usernam == '' and mail != '':
                usera = User.objects.filter(email=mail)
                if len(usera) == 0:
                    return render(request, 'basededonnee/oublie.html',{'form':form,'rate':1})
                if len(usera) > 1:
                    return render(request, 'basededonnee/oublie.html',{'form':form,'rate':3})
                usera = User.objects.filter(email=mail)[0]

            if len (Parent.objects.filter(userP=usera)) == 0:
                return render(request, 'basededonnee/oublie.html',{'form':form,'rate':4})
            password = str(random.randrange(1000000,10000000))
            usera.set_password(password)
            usera.save()
            ctx = {
                'utilisateur' : usera.username,
                'password' : password
            }
            objet = 'Kidscov identifiants oubliés'
            message = get_template('mail/test.html').render(Context(ctx))
            to = [usera.email,settings.EMAIL_HOST_USER]
            msg = EmailMessage(objet,message,to=to,from_email=settings.EMAIL_HOST_USER)
            msg.content_subtype = 'html'
            msg.send()
            return render(request, 'basededonnee/oublie.html',{'gg':1})     
    return render(request, 'basededonnee/oublie.html',{'form':form})
    

def covoiturage(request):
    if  len (Enfant.objects.filter(userE_id = request.user.id)):    # si l'user est un enfant
        USER = Enfant.objects.filter(userE_id = request.user.id)[0]
        passager = Passager.objects.filter(enf = USER.id )          # prendre les covoits où il est passager
        covoit =[]                                                  
        for i in range (len(passager)):
            covoit.append(Covoiturage.objects.filter(id = passager[i].covoit)[0])
    else:
        USER = Parent.objects.filter(userP_id = request.user.id)[0]
        covoit = Covoiturage.objects.filter(conducteur = USER)
    return render(request, 'basededonnee/covoiturage.html',{'covoit':covoit})


def magie():
    Ec = Ecole.objects.all()
    
    ##_Lundi_##
    D = Disponibilite.objects.filter(jour='L')
    C = covUtil.objects.filter(jour='L')
    for i in range (len(Ec)):
        E = Enfant.objects.filter(Ecole = Ec[i])
        ListeEnfant = []
        ListeParent = []
        for j in range (len(E)):
            if E[j].EDT.L.Matin == '08:00:00':
                ListeEnfant.appendE[j]
        for j in range (len(D)):
            if pow(E[i].adresse.x-D[j].LieuCollecte.x,2) + pow(E[i].adresse.y-D[j].LieuCollecte.y,2) < 100 :
                ListeParent.append(D[j])
            

    
def cov(Usera,joura,HD,HA,LD,LA):
    c = covUtil.objects.filter(Usr=Usera,jour=joura)
    Usera_id = User.objects.filter(id=Usera)[0].id
    if len(c) == 0:
        if HA == False and LA != False:
            c = covUtil.objects.create(Usr_id=Usera,jour=joura,horaireDepart=HD,LieuDepart=LD,LieuArrivee=LA)
            c.save()
        elif HA != False and LA != False:
            c = covUtil.objects.create(Usr=Usera,jour=joura,horaireDepart=HD,horaireArrivee=HA,LieuDepart=LD,LieuArrivee=LA)
            c.save()
        elif HA == False and LA == False:
            c = covUtil.objects.create(Usr=Usera,jour=joura,horaireDepart=HD,LieuDepart=LD)
            c.save()
        elif HA != False and LA == False:
            c = covUtil.objects.create(Usr=Usera,jour=joura,horaireDepart=HD,horaireArrivee=HA,LieuDepart=LD)
            c.save()
    else:
        c=c[0]
        c.Usr_id=Usera
        c.jour=joura
        c.horaireDepart=HD
        c.LieuDepart=LD
        if HA != False:
            c.horaireArrivee=HA
        if LA != False:
            c.LieuArrivee=LA
        c.save()
    print(c)

def modifierEdt(request,ida,jour):
    UserP = request.user
    parent = Parent.objects.filter(userP_id=UserP.id)[0]
    enfant = Enfant.objects.filter(id=ida)[0]
    UserE = User.objects.filter(id=enfant.userE_id)[0]
    Edt = enfant.EDT
    if request.method == 'POST':
        j = JourneeFormulaire(request.POST)
        j.fields['LieuM'].queryset = Lieu.objects.filter(proprietaire_id=UserP.id)
        j.fields['LieuS'].queryset = Lieu.objects.filter(proprietaire_id=UserP.id)
        if j.is_valid():
            lm = request.POST.get('Matin')
            ls = request.POST.get('Soir')
            LM = request.POST.get('LieuM')
            LS = request.POST.get('LieuS')

            if jour == 'L':
                Edt.L.Matin=lm
                Edt.L.Soir=ls
                Edt.L.LieuM=Lieu.objects.filter(id=LM)[0]
                Edt.L.LieuS=Lieu.objects.filter(id=LS)[0]
                cov(UserE.id,'L',Edt.L.Matin,False,Edt.L.LieuM,enfant.Ecole.Adresse)
                cov(UserE.id,'L',Edt.L.Soir,False,enfant.Ecole.Adresse,Edt.L.LieuS)
                Edt.L.save()
            if jour == 'M':
                Edt.M.Matin=lm
                Edt.M.Soir=ls
                Edt.M.LieuM=Lieu.objects.filter(id=LM)[0]
                Edt.M.LieuS=Lieu.objects.filter(id=LS)[0]
                cov(UserE.id,'M',Edt.M.Matin,False,Edt.M.LieuM,enfant.Ecole.Adresse)
                cov(UserE.id,'M',Edt.M.Soir,False,enfant.Ecole.Adresse,Edt.M.LieuS)
                Edt.M.save()
            if jour == 'D':
                Edt.D.Matin=lm
                Edt.D.Soir=ls
                Edt.D.LieuM=Lieu.objects.filter(id=LM)[0]
                Edt.D.LieuS=Lieu.objects.filter(id=LS)[0]
                cov(UserE.id,'D',Edt.D.Matin,False,Edt.D.LieuM,enfant.Ecole.Adresse)
                cov(UserE.id,'D',Edt.D.Soir,False,enfant.Ecole.Adresse,Edt.D.LieuS)
                Edt.Mer.save()
            if jour == 'J':
                Edt.J.Matin=lm
                Edt.J.Soir=ls
                Edt.J.LieuM=Lieu.objects.filter(id=LM)[0]
                Edt.J.LieuS=Lieu.objects.filter(id=LS)[0]
                cov(UserE.id,'J',Edt.J.Matin,False,Edt.J.LieuM,enfant.Ecole.Adresse)
                cov(UserE.id,'J',Edt.J.Soir,False,enfant.Ecole.Adresse,Edt.J.LieuS)
                Edt.J.save()
            if jour == 'V':
                Edt.V.Matin=lm
                Edt.V.Soir=ls
                Edt.V.LieuM=Lieu.objects.filter(id=LM)[0]
                Edt.V.LieuS=Lieu.objects.filter(id=LS)[0]
                cov(UserE.id,'V',Edt.V.Matin,False,Edt.V.LieuM,enfant.Ecole.Adresse)
                cov(UserE.id,'V',Edt.V.Soir,False,enfant.Ecole.Adresse,Edt.V.LieuS)
                Edt.V.save()
            if jour == 'S':
                Edt.S.Matin=lm
                Edt.S.Soir=ls
                Edt.S.LieuM=Lieu.objects.filter(id=LM)[0]
                Edt.S.LieuS=Lieu.objects.filter(id=LS)[0]
                cov(UserE.id,'S',Edt.S.Matin,False,Edt.S.LieuM,enfant.Ecole.Adresse)
                cov(UserE.id,'S',Edt.S.Soir,False,enfant.Ecole.Adresse,Edt.S.LieuS)
                Edt.S.save()
            
            Edt.save()
            enfant.save()
            red = '/home/enfant/'+str(enfant.id) + '/'
            return HttpResponseRedirect(red)
    else:
        if jour == 'L':
            j = JourneeFormulaire(instance = Edt.L)
        if jour == 'M':
            j = JourneeFormulaire(instance = Edt.M)
        if jour == 'D':
            j = JourneeFormulaire(instance = Edt.D)
        if jour == 'J':
            j = JourneeFormulaire(instance = Edt.J)
        if jour == 'V':
            j = JourneeFormulaire(instance = Edt.V)
        if jour == 'S':
            j = JourneeFormulaire(instance = Edt.S)
        j.fields['LieuM'].queryset = Lieu.objects.filter(proprietaire_id=UserP.id)
        j.fields['LieuS'].queryset = Lieu.objects.filter(proprietaire_id=UserP.id)
    return render(request, 'basededonnee/voirEdt.html', {'form':j,'id':UserE.id, 'ida':ida})

def modifier(request):
    ida=request.user.id
    user = User.objects.filter(id=ida)[0]

    UserPa = Parent.objects.filter(userP_id=user.id)[0]
    username = user.username
    if request.method =='POST':
        form = voirParent(request.POST)
        if form.is_valid():
            email = request.POST.get('Email')
            first = request.POST.get('Prenom')
            last = request.POST.get('Nom')
            yp = request.POST.get('yourpass')
            p1=request.POST.get('p1')
            p2=request.POST.get('p2')

            UserPa.Numero_Telephone = request.POST.get('Numero_Telephone')
            UserPa.Immatriculation = request.POST.get('Immatriculation')
            UserPa.Couleur_voiture = request.POST.get('Couleur_voiture')
            UserPa.Nombre_place = request.POST.get('Nombre_place')
            UserPa.Prenom=first
            UserPa.Nom=last
            UserPa.Email=email
            
            user.first_name=first
            user.last_name=last
            user.email=email

            if(user.check_password(yp) == True):
                if(p1 == p2):
                    user.set_password(p1)
            
            UserPa.save()
            user.save()
            UserPa.save()
            return redirect('/home/modifier/')
    else:
        form=voirParent(instance=UserPa)
    return render(request, 'basededonnee/modifier.html', {'form': form,'username':username})

def supprimerEnfant(request,ida):
    enf = Enfant.objects.filter(id=ida)[0]
    UserE = User.objects.filter(id=enf.userE.id)[0]
    A = covUtil.objects.filter(Usr = UserE)
    for i in range (len(A)):
        A[i].delete()
    enf.delete()
    return redirect('/home/enfant')

def ajouterEcole(request,ida):
    form = EcoleFormulaire2()
    if request.method == 'POST':
        form = EcoleFormulaire2(request.POST)
        if form.is_valid():
            test = Lieu.objects.create()
            test.Nom = request.POST.get('Nom')
            test.Adresse = request.POST.get('Adresse')
            test.Code_postal = request.POST.get('Code_postal')
            test.Numero_rue = request.POST.get('Numero_rue')
            test.Ville = request.POST.get('Ville')
            E = Ecole.objects.create(Adresse=test)
            test.save()
            E.save()
            red = '/home/enfant/'+ida+'/Ecole/'
            return redirect(red)
    return render(request, 'basededonnee/ajouterEcole.html',{'form':form,'ida':ida})
    

def modifierEcole(request,ida):
    enf = Enfant.objects.filter(id=ida)[0]
    if request.method == 'POST':
        form = EcoleFormulaire(request.POST)
        if form.is_valid:
            ecole = request.POST.get('Ecole')
            enf.Ecole = Ecole.objects.filter(id=ecole)[0]
            enf.save()
            red = '/home/enfant/'+ida+'/Ecole/'
            return redirect(red)
    form = EcoleFormulaire(instance=enf)
    return render(request, 'basededonnee/modifierEcole.html',{'form':form,'ida':ida})

def voirenfant(request,ida):
    user = request.user
    enf = Enfant.objects.filter(id=ida)[0]
    Uenf = User.objects.filter(id=enf.userE_id)[0]
    username = Uenf.username
    if len ( Edt.objects.filter(id=enf.EDT_id)) == 0:
        supprimerEnfant(request,ida)
        
    EDT = Edt.objects.filter(id=enf.EDT_id)[0]
    Ecole=enf.Ecole
    if request.method== 'POST':
        form=VoirEnfant(request.POST)
        if form.is_valid():
            fn=request.POST.get('first_name')
            ln = request.POST.get('last_name')
            p = request.POST.get('password')
            p1 = request.POST.get('p1')
            p2 = request.POST.get('p2')

            Uenf.first_name=fn
            Uenf.last_name=ln
            if(user.check_password(p) == True):
                if(p1 == p2):
                    user.set_password(p1)
            Uenf.save()
            
            red = '/home/enfant/'+str(ida) + '/'
            return redirect(red)
    else:
        form=VoirEnfant(instance=Uenf)
    return render(request, 'basededonnee/voirenfant.html', {'form': form,'username':username, 'EDT' : EDT,'ida':ida,'Ecole':Ecole})

def accueil(request):
    User = request.user
    Paren = Parent.objects.filter(userP_id = User.id)
   # print("ici")
   # if Paren[0].photo == "":
   #     photo = File(open("/home/zacchello/travail/s8/pfa/covoiturage/Media/nope.jpg",'r'))
   # print("ici")
    isParent=0
    if( len(Paren) == 1):
        isParent=1
        return render(request, 'basededonnee/accueil.html',{'isParent' : isParent, 'photo':"/home/zacchello/travail/s8/pfa/covoiturage/Media/nope.jpg"})
    return render(request, 'basededonnee/accueil.html',{'isParent' : isParent})

def supprimerDispo(request,ida):
    disp = Disponibilite.objects.filter(id=ida)[0]
    cov = covUtil.objects.filter(Usr=request.user,jour=disp.jour)
    disp.delete()
    return redirect('/home/dispo')
    
    
def voiradresse(request,id):
    adresse = Lieu.objects.filter(id=id)[0]
    #String = adresse.Numero_rue +" "+ adresse.Adresse +" "+ adresse.Ville +" "+ adresse.Code_postal
    String = adresse.Adresse +" "+ adresse.Ville +" "+ adresse.Code_postal
    geocode_result = gmaps.geocode(String)
    inst = Lieu.objects.filter(id=id)[0]
    formu=LieuFormulaire(instance=inst)
    if geocode_result!=[]:
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']
        lat = str(latitude)
        lng = str(longitude)
        adresse.x = longitude
        adresse.y = latitude
    if request.method == 'POST':
        form = LieuFormulaire(request.POST)
        if form.is_valid():
            test = Lieu.objects.filter(id=id)[0]
            test.Nom = request.POST.get('Nom')
            test.Adresse = request.POST.get('Adresse')
            test.Code_postal = request.POST.get('Code_postal')
            test.Numero_rue = request.POST.get('Numero_rue')
            test.Ville = request.POST.get('Ville')
            test.save()
            red = '/home/voiradresse/'+ id + '/'
            return HttpResponseRedirect(red)
    else:    
        formu=LieuFormulaire(instance=inst)
        
    if geocode_result!=[]:
        return render(request, 'basededonnee/voiradresse.html',{'latitude' : lat, 'longitude' : lng, 'form':formu})
    else:
        return render(request, 'basededonnee/voiradresse.html',{'form':formu})

def ajoutDisponibilite(request):
    user = request.user
    if request.method == 'POST':
        form = DisponibiliteFormulaire(request.POST)
        form.fields['LieuCollecte'].queryset = Lieu.objects.filter(proprietaire_id=user.id)
        if(form.is_valid()):
            #jour = request.POST.get('jour')
            debut = request.POST.get('debut')
            fin = request.POST.get('fin')
            jour = request.POST.get('jour')
            lieu = request.POST.get('LieuCollecte')
           # retour = request.POST.get('retour')
            #récuperer l'id du parent en connaissant celui de l'utilisateur courant
            
            parent = Parent.objects.filter(userP_id = request.user.id)
            ida = parent[0].id
            disp = Disponibilite.objects.create(debut=debut,fin=fin)
            lieu = Lieu.objects.filter(id=lieu)[0]
            disp.userP_id=ida
            disp.debut = debut
            disp.fin = fin
            disp.jour=jour
            disp.LieuCollecte = lieu
        #    disp.retour=retour
            disp.save()
            return redirect('/home/dispo')
    else:
        form=DisponibiliteFormulaire()
        form.fields['LieuCollecte'].queryset = Lieu.objects.filter(proprietaire_id=user.id)
    return render(request, 'basededonnee/ajoutDispo.html', {'form': form})

#def gererationCovoiturage():
    
         
def adresse(request):
    User = request.user
    liste = Lieu.objects.filter(proprietaire_id=User.id)
    parent = Parent.objects.filter(userP = User)[0]
    adresse = parent.Lieu
    form = AdresseFormulaire()
    form.fields['Lieu'].queryset = Lieu.objects.filter(proprietaire_id=User.id)
    form.fields['Lieu'].initial=adresse
    if request.method == 'POST':
        form = AdresseFormulaire(request.POST)
        if form.is_valid:
            Lieua = request.POST.get('Lieu')
            if Lieua == '':
                form = AdresseFormulaire()
                form.fields['Lieu'].queryset = Lieu.objects.filter(proprietaire_id=User.id)
                form.fields['Lieu'].initial=adresse
                return render(request, 'basededonnee/adresse.html',{'liste':liste,'defaut':adresse,'form':form})
                
            L = Lieu.objects.filter(id=Lieua)
            if len (L) == 0:
                form = AdresseFormulaire(instance = adresse)
                form.fields['Lieu'].queryset = Lieu.objects.filter(proprietaire_id=User.id)
                form.fields['Lieu'].initial=adresse
                return render(request, 'basededonnee/adresse.html',{'liste':liste,'defaut':adresse,'form':form})
            
            L = Lieu.objects.filter(id=Lieua)[0]
            parent.Lieu = L
            parent.save()
            return redirect('/home/adresse/')
    
    return render(request, 'basededonnee/adresse.html',{'liste':liste,'defaut':adresse,'form':form})

def ajoutAdresse(request):
    if request.method =='POST':
        form = LieuFormulaire(request.POST)
        if form.is_valid():
            Nom = request.POST.get('Nom')
            Adresse = request.POST.get('Adresse')
            Code_postal = request.POST.get('Code_postal')
            #Numero_rue = request.POST.get('Numero_rue')
            Ville = request.POST.get('Ville')
            
            lieu = Lieu.objects.create(Nom=Nom)
            lieu.Adresse=Adresse
            lieu.Code_postal=Code_postal
            #lieu.Numero_rue=Numero_rue
            lieu.Ville=Ville
            lieu.proprietaire_id=request.user.id

            #String = lieu.Numero_rue +" "+ lieu.Adresse +" "+ lieu.Ville +" "+ lieu.Code_postal
            String = lieu.Adresse +" "+ lieu.Ville +" "+ lieu.Code_postal
            geocode_result = gmaps.geocode(String)
            print(geocode_result[0])
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
            lieu.x = longitude
            lieu.y = latitude            
            lieu.save()
            return redirect('/home/')
    else:
        form=LieuFormulaire()
    return render(request, 'basededonnee/ajoutAdresse.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
            else:
                error=True
    else:
        form=ConnexionForm()
    return render(request, 'basededonnee/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return render(request,'basededonnee/accueil.html',locals())

def inscription(request):
    if request.method =='POST':
        form = ParentFormulaire(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first = request.POST.get('first_name')
            last = request.POST.get('last_name')
            user = User.objects.create_user(username,email, password)
            user.first_name=first
            user.last_name=last
            user.published_date = datetime.now()
            user.save()
            p = Parent.objects.create(userP_id=user.id)
            
            #p.photo = '/nope.jpg'
            p.Prenom=first
            p.Nom=last
            p.Email=email
            p.save()
            send_mail('Hello', 'Body goes here',settings.EMAIL_HOST_USER,[email], fail_silently=False)
            return redirect('/home/')
    else:
        form=ParentFormulaire()
    return render(request, 'basededonnee/inscription.html', {'form': form})

def ajoutEnfant(request):
    if request.method == 'POST':
        form = EnfantFormulaire(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            first = request.POST.get('first_name')
            last = request.POST.get('last_name')
            user = User.objects.create_user(username)
            user.set_password(password)
            user.first_name=first
            user.last_name=last
            user.published_date = datetime.now()
            user.save()

            #récuperer l'id du parent en connaissant celui de l'utilisateur courant
            parent = Parent.objects.filter(userP_id = request.user.id)
            ida = parent[0].id
            #request.user.id = User.id not Parent.id
            
            E= Enfant.objects.create(userE_id=user.id,parent_id=ida)
            Li = parent[0].Lieu
            l = Journee.objects.create(jour='Lundi')
            l.LieuM = Li
            l.LieuS = Li
            l.save()
            m = Journee.objects.create(jour='Mardi')
            m.LieuM = Li
            m.LieuS = Li
            m.save()
            mer = Journee.objects.create(jour='Mercredi')
            mer.LieuM = Li
            mer.LieuS = Li
            mer.save()
            j = Journee.objects.create(jour='Jeudi')
            j.LieuM = Li
            j.LieuS = Li
            j.save()
            v = Journee.objects.create(jour='Vendredi')
            v.LieuM = Li
            v.LieuS = Li
            v.save()
            s = Journee.objects.create(jour='Samedi')
            s.LieuM = Li
            s.LieuS = Li
            s.save()
            edt=Edt.objects.create(L=l,M=m,D=mer,J=j,V=v,S=s)
            E.EDT=edt
            E.save()
            return redirect('/home/enfant/')
    else:
        form=EnfantFormulaire()
    return render(request, 'basededonnee/ajoutEnfant.html', {'form': form})

def voirenfants(request):
    id = request.user
    parent = Parent.objects.filter(userP_id = id)
    if(len(parent) == 0):
        return render(request, 'basededonnee/enfant.html',locals())
    else:
        liste = Enfant.objects.filter(parent_id=parent[0].id)
        return render(request, 'basededonnee/enfant.html',{'liste':liste})

    
def disponibilite(request):
    id = request.user
    parent = Parent.objects.filter(userP_id = id)
    if(len(parent) == 0):
        return render(request, 'basededonnee/dispo.html',locals())
    else:
        liste = Disponibilite.objects.filter(userP_id=parent[0].id)
        return render(request, 'basededonnee/dispo.html',{'liste':liste})
    
