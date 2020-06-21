from tkinter import *
from functools import partial
from base import *
from fenetre import *



def mdp(f, text, e_user, e_mdp): # Validation de l'authentification à la base de donnée
    try: # Test
        user = e_user.get()
        mp = e_mdp.get()
        baseConnection(user, mp) 
        f.destroy()
        win = Tk()
        fen(win,2)
    except: # Sinon
        e_user.delete(0, END)
        e_mdp.delete(0, END)
        text.config(text="Nom ou mot de passe incorecte(s), veuillez réessayer")
        

def don_pat(f,  Id, t2, e_nom, e_prenom, e_sexe, e_date, e_autre, e_traitement): # Validation des donnée du patient pour la création et ma modification
    # Pour Id == 0 : Création du Patient ; Sinon : Modification
    a, b = "a", "b" #Variable a et b sont là pour valider par la suite que certainne chose sont faisable voire suite (Try)
    nom = e_nom.get()
    prenom = e_prenom.get()
    sexe = e_sexe.get()
    date = e_date.get()
    autre = e_autre.get()
    traitement = e_traitement.get()
    nom = nom.upper()
    if prenom == '' or len(prenom) >= 45:
        t2.config(text="Certains champs obligatoires sont mal renseigné (* : Les champs sont obligtoire)")
    else:
        if sexe == "M" or sexe == "F" or sexe == "" and len(nom) <= 45 and len(autre) <= 255 and len(traitement) <= 255:
            a = 1 # Ici, si sexe ou nom pas bon, alors a = 1 sinon a = "a"
        try:
            a = int(a) # Donc si sexe ou nom pas bon, on s'arrête là
            d = int(date)
            if len(date) == 8 and int(date[4:6]) <= 12 and int(date[6:8]) <= 31:
                b = 1
            b = int(b)
            if Id == 0:
                baseCreatPat(prenom, nom, sexe, date, autre, traitement, True)
                e_nom.delete(0, END)
                e_prenom.delete(0, END)
                e_sexe.delete(0, END)
                e_date.delete(0, END)
                e_autre.delete(0, END)
                e_traitement.delete(0, END)
            else:
                baseModifPat(Id, prenom, nom, sexe, date, autre, traitement, True)

            t2.config(text = "Veuillez saisir les champs (* : Les champs sont obligatoire)")
        except:
            if a == 1 and date == "":
                if Id == 0:
                    baseCreatPat(prenom, nom, sexe, date, autre, traitement, False)
                    e_nom.delete(0, END)
                    e_prenom.delete(0, END)
                    e_sexe.delete(0, END)
                    e_date.delete(0, END)
                    e_autre.delete(0, END)
                    e_traitement.delete(0, END)
                else:
                    baseModifPat(Id, prenom, nom, sexe, date, autre, traitement, False)
                t2.config(text = "Veuillez saisir les champs (* : Les champs sont obligatoire)")
            else:
                t2.config(text="Certains champs optionel sont mal renseigné (* : Les champs sont obligatoire)")
                    
        
def graph(Id, text_1, text_2, text_3, var_, t_):
    var = []
    t = []
    for i in range (len(var_)):
        var.append(var_[i].get())
    for i in range(len(t_)):
        t.append(t_[i].get())
          
    if var == [0,0,0,0] and t != [0,0,0]:
        text_1.config(text="Veuillez sélectionner une case dans capteur")
        text_2.config(fg="red")
        text_3.config(fg="black")
          
    elif var == [0,0,0,0] and t == [0,0,0]:
        text_1.config(text="Veuillez sélectionner une case dans capteur et dans temps")
        text_2.config(fg="red")
        text_3.config(fg="red")
          
    elif var != [0,0,0,0] and t == [0,0,0]:
        text_1.config(text="Veuillez sélectionner une case dans temps")
        text_2.config(fg="black")
        text_3.config(fg="red")
          
    else:
        text_1.config(text="Que voulez vous savoir ?")
        text_2.config(fg="black")
        text_3.config(fg="black")
        type_prise = []
        if var[0] == 1: # Le poux
            type_prise.append(1)
        if var[1] == 1: # La tension
            type_prise.append(2) # Tension diastolique
            type_prise.append(3) # Tension systolique
        if var[2] == 1: # Le SpO2
            type_prise.append(4)
        if var[3] == 1: # La température
            type_prise.append(5)
        if t[0] == 1 : # Pour 1h
            ok = baseDemandDon(Id, 1, type_prise)
        if t[1] == 1: # Pour 6h
            ok = baseDemandDon(Id, 6, type_prise)
        if t[2] == 1: #Pour 24h
            ok = baseDemandDon(Id, 24, type_prise)


