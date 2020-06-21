from tkinter import *
from functools import partial
import valid as v
from base import *


def retour(f, nb): # En appuyant sur un des boutons "Retour" des différentes fenêtres
    if nb == 1: # Destruction de tous
        f.destroy()
    elif nb == 2: # Déconnection de la base
        baseQuit()
        f.destroy()
        fen(Tk(), 1)
    else: # Retour à la fenêtre n°2
        f.destroy()
        fen(Tk(), 2)




def validation(nb, quant, f, *args): # En appuyant sur un des boutons "Valider" des différentes fenêtres (prise en charge au cas par cas grace à nb donné en appelant fen)
    if nb == 1: 
        v.mdp(f, *args)
        
    elif nb == 2: # "quant" est le numéro de sélection
        if quant == 1: # Création Pat
            f.destroy()
            fen(Tk(), 3)
        elif quant == 2: # Modification Pat
            f.destroy()
            fen(Tk(), 4)
        elif quant == 3: # Visualisation Courbes
            f.destroy()
            fen(Tk(), 6)
            
    elif nb == 3: # Pour quant = 0, dans don_pat on prends la création d'un nouveau patient
        quant = 0
        v.don_pat(f, quant, *args)

    elif nb == 5: # "quant" est l' Id du Patient pour la Modif
        v.don_pat(f, quant, *args)

    elif nb == 4 or nb == 6: # "quant" est le str sélectionné dans la liste qui passe en int par la suite pour faire l' Id
        if quant[2] == " ": # Ici l' Id peut aller que jusqu'a 999
            a = quant[0]+quant[1]
            Id = int(a)
        elif quant[3] == " ":
            a = quant[0]+quant[1]+quant[2]
            Id = int(a)
        else:
            Id = int(quant[0])
        f.destroy()
        win = Tk()
        if nb == 4:
            fen(win, 5, Id)
        else:
            fen(win, 7, Id)
            
    elif nb == 7: # "quant" est l' Id du patient ou l'on veut le graph
        v.graph(quant, *args)



     
def fen(f, nb, Id = 0):
    quitter = partial(retour, f, nb) # partial permet d'appeler une fonction avec arguments : partial(nom_fonction, *args)
    f.title("controle_patient.exe")
    
    if nb == 1: # Page de connection à la base de donnée
        text = Label (f, text = "Connection : ")
        text_user = Label(f, text="Nom d'utilisateur : ")
        entre_user = Entry(f)
        text_mdp = Label(f, text="Mot de passe : ")
        entre_mdp = Entry(f, show = "*")
        valid = partial(validation, nb, nb, f, text, entre_user, entre_mdp)
        bouton_valid = Button(f, text="Valider", command=valid)
        bouton_quitter = Button(f, text="Quitter", command=quitter)

        text.grid(row=0, column=0, columnspan=4, pady=10)
        text_user.grid(row=1, column=0, padx=(20,0))
        entre_user.grid(row=1, column=1, padx=(20,0))
        text_mdp.grid(row=2, column=0, padx=(20,0))
        entre_mdp.grid(row=2, column=1, padx=(20,0))
        bouton_valid.grid(row=3, column=2)
        bouton_quitter.grid(row=4, column=3, padx=(20,0), pady=(20,0))
        
    elif nb== 2: # Page de sélection (Création, modification ou visualisation des courbes d'un patient)
        text = Label(f, text="Que voulez vous faire ? ")
        valid = partial(validation, nb, 1, f)
        bouton_p3 = Button(f, text="Création d'un patient", command=valid)
        valid = partial(validation, nb, 2, f)
        bouton_p4 = Button(f, text="Modification d'un patient", command=valid)
        valid = partial(validation, nb, 3, f)
        bouton_p5 = Button(f, text="Interface de prélevement", command=valid)
        bouton_quitter = Button(f, text="Déconnection", command=quitter)

        text.grid(row=0, column=0, columnspan=2, pady=10)
        bouton_p3.grid(row=1, column=0, padx=(20,0), pady=5)
        bouton_p4.grid(row=2, column=0, padx=(20,0), pady=5)
        bouton_p5.grid(row=3, column=0, padx=(20,0), pady=5)
        bouton_quitter.grid(row=4, column=1, padx=(20,0), pady=(20,0))
        
    elif nb == 3: # Page de création d'un nouveau patient
        t1 = Label(f, text = "Création dans la base d'un nouveau patient")
        t2 = Label(f, text = "Veuillez saisir les champs (* : Les champs sont obligatoire)")
        t_nom = Label(f, text = "Nom : ")
        e_nom = Entry(f)
        t_prenom = Label(f, text = "Prénom : * ")
        e_prenom = Entry(f)
        t_sexe = Label(f, text = "Sexe (M ou F) : ")
        e_sexe = Entry(f)
        t_date = Label(f, text = "Date de naissance (AAAAMMJJ) : ")
        e_date = Entry(f)
        t_autre = Label(f, text = "Infos complémentaire (maladies chroniques, alergies...) : ")
        e_autre = Entry(f)
        t_traitement = Label(f, text = "Traitement que prend le patients : ")
        e_traitement = Entry(f)
        valid = partial(validation, nb, 0, f, t2, e_nom, e_prenom, e_sexe, e_date, e_autre, e_traitement)
        b_valid = Button(f, text = "Valider", command=valid)
        b_quitter = Button(f, text = "Retour", command=quitter)

        t1.grid(row=0, column=0, columnspan=4, pady=10)
        t2.grid(row=1, column=0, columnspan=4, pady=10)
        t_nom.grid(row=3, column=0, padx=(20,0), pady=2)
        e_nom.grid(row=3, column=1, padx=(20,0), pady=2)
        t_prenom.grid(row=4, column=0, padx=(20,0), pady=2)
        e_prenom.grid(row=4, column=1, padx=(20,0), pady=2)
        t_sexe.grid(row=5, column=0, padx=(20,0), pady=2)
        e_sexe.grid(row=5, column=1, padx=(20,0), pady=2)
        t_date.grid(row=6, column=0, padx=(20,0), pady=2)
        e_date.grid(row=6, column=1, padx=(20,0), pady=2)
        t_autre.grid(row=7, column=0, padx=(20,0), pady=2)
        e_autre.grid(row=7, column=1, padx=(20,0), pady=2)
        t_traitement.grid(row=8, column=0, padx=(20,0), pady=2)
        e_traitement.grid(row=8, column=1, padx=(20,0), pady=2)
        b_valid.grid(row=9, column=2, padx=(20,0))
        b_quitter.grid(row=10, column=3, padx=(20,0), pady=(20, 0))

    elif nb == 4 or nb == 6: # Page de sélection de la fiche du patient à modifier ou à voire (4 ou 6)
        def clic(evt):
            i = listbox.curselection()
            i = listbox.get(i)
            validation(nb, i, f)
        t1 = Label(f, text="Modification dans la base un patient")
        listbox = Listbox(f)
        baseListPat(listbox)
        listbox.bind('<ButtonRelease-1>', clic)
        b_quit = Button(f, text="Retour", command=quitter)
        t1.grid(row=0, column=0, columnspan=3, pady=10)
        listbox.grid(row=1, column=0, padx=(20,0))
        b_quit.grid(row=3, column=2, padx=(20,0), pady=(20, 0))

    elif nb == 5: # Page de modification de la fiche du patient sélectionné en page 4
        resultat = baseDonPat(Id)
        texte = "Modification dans la base du patient "+resultat[0]+" "+resultat[1]
        t1 = Label(f, text = texte)
        t2 = Label(f, text = "Veuillez saisir les champs (* : Les champs sont obligatoire)")
        t_nom = Label(f, text = "Nom : ")
        e_nom = Entry(f)
        t_prenom = Label(f, text = "Prénom : * ")
        e_prenom = Entry(f)
        t_sexe = Label(f, text = "Sexe (M ou F) : ")
        e_sexe = Entry(f)
        t_date = Label(f, text = "Date de naissance (AAAAMMJJ) : ")
        e_date = Entry(f)
        t_autre = Label(f, text = "Infos complémentaire (maladies chroniques, alergies...) : ")
        e_autre = Entry(f)
        t_traitement = Label(f, text = "Traitement que prend le patients : ")
        e_traitement = Entry(f)
                # Mise en place des infos déjà renseigné
        e_nom.insert(END, str(resultat[0]))
        e_prenom.insert(END, str(resultat[1]))
        e_sexe.insert(END, str(resultat[2]))
        e_date.insert(END, str(resultat[3]))
        e_autre.insert(END, str(resultat[4]))
        e_traitement.insert(END, str(resultat[5]))
        
        valid = partial(validation, nb, Id, f, t2, e_nom, e_prenom, e_sexe, e_date, e_autre, e_traitement)
        b_valid = Button(f, text = "Valider", command=valid)
        b_quitter = Button(f, text = "Retour", command=quitter)
        

        
        t1.grid(row=0, column=0, columnspan=4, pady=10)
        t2.grid(row=1, column=0, columnspan=4, pady=10)
        t_nom.grid(row=3, column=0, padx=(20,0), pady=2)
        e_nom.grid(row=3, column=1, padx=(20,0), pady=2)
        t_prenom.grid(row=4, column=0, padx=(20,0), pady=2)
        e_prenom.grid(row=4, column=1, padx=(20,0), pady=2)
        t_sexe.grid(row=5, column=0, padx=(20,0), pady=2)
        e_sexe.grid(row=5, column=1, padx=(20,0), pady=2)
        t_date.grid(row=6, column=0, padx=(20,0), pady=2)
        e_date.grid(row=6, column=1, padx=(20,0), pady=2)
        t_autre.grid(row=7, column=0, padx=(20,0), pady=2)
        e_autre.grid(row=7, column=1, padx=(20,0), pady=2)
        t_traitement.grid(row=8, column=0, padx=(20,0), pady=2)
        e_traitement.grid(row=8, column=1, padx=(20,0), pady=2)
        b_valid.grid(row=9, column=2, padx=(20,0))
        b_quitter.grid(row=10, column=3, padx=(20,0), pady=(20, 0))
  
    elif nb == 7: # Page de sélection des critères de visionnage
          
        text_1 = Label(f, text="Que voulez vous savoir ?")
        text_2 = Label(f, text="Capteur")
        text_3 = Label(f, text="Temps")
        
        var_1, var_2, var_4, var_5 = IntVar(), IntVar(), IntVar(), IntVar()
        t_1, t_2, t_3 = IntVar(), IntVar(), IntVar()  
        cb_1 = Checkbutton(f, text="Poul", variable=var_1, activebackground="gray")
        cb_2 = Checkbutton(f, text="Tension", variable=var_2, activebackground="gray")
        cb_4 = Checkbutton(f, text="SpO2", variable=var_4, activebackground="gray")
        cb_5 = Checkbutton(f, text="Température", variable=var_5, activebackground="gray")
        tcb_1 = Checkbutton(f, text="1h", variable=t_1, activebackground="gray")
        tcb_2 = Checkbutton(f, text="6h", variable=t_2, activebackground="gray")
        tcb_3 = Checkbutton(f, text="24h", variable=t_3, activebackground="gray")
        #cb_1 : Poul                   tcb_1 : 1H
        #cb_2 : Tension  (haute/basse)          tcb_2 : 6H
        #cb_4 : SpO2                  tcb_3 : 24H
        #cb_5 : Température
        var = (var_1, var_2, var_4, var_5)
        t = (t_1, t_2, t_3)
        valid = partial(validation, nb, Id, f, text_1,text_2, text_3, var, t)
        bouton_valid = Button(f, text="Valider", command=valid)
        bouton_quitter = Button(f, text="Retour", command=quitter)
        
        text_1.grid(row=0, column=0, columnspan=4, pady=10)
        text_2.grid(row=1, column=0, padx=(20,0))
        text_3.grid(row=1, column=1, padx=(20,0))
        cb_1.grid(row=2, column=0, padx=(20,0))
        cb_2.grid(row=3, column=0, padx=(20,0))
        cb_4.grid(row=4, column=0, padx=(20,0))
        cb_5.grid(row=5, column=0, padx=(20,0))
        tcb_1.grid(row=2, column=1, padx=(20,0))
        tcb_2.grid(row=3, column=1, padx=(20,0))
        tcb_3.grid(row=4, column=1, padx=(20,0))
        bouton_valid.grid(row=6, column=2, padx=(20,0))
        bouton_quitter.grid(row=7, column=3, padx=(20,0), pady=(20,0))


if __name__ == '__main__':
    win = Tk()
    fen(win,1)
    mainloop()
