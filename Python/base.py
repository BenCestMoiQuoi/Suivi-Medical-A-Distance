from tkinter import *
from functools import partial
#from valid import *
import pymysql.cursors
import datetime
from exploitation import *

def virgule(text, t_rajout):
    if text == "":
        return ""
    else:
        return str(t_rajout)

def baseConnection(name, mdp): # Connection à la base de donné
    global connection
    connection = pymysql.connect(host = 'localhost',
                                 user= name ,
                                 password = mdp)
    print("Connection éffectué")
    

def baseQuit(): # Déconnection de la base de donné
    global connection
    connection.close()
    print("Déconnection éffectué")

def baseCreatPat(prenom, nom, sexe, date, autre, traitement, valid): # Création dans la base d'un patient
    global connection
    cursor = connection.cursor()
    if valid:
        sql = "INSERT INTO TIPE.PATIENTS (Nom, Prenom, Sexe, Date_nais, Autre, Traitement, Date_creat, Date_der_modif)"\
              +"values (%s, %s, %s, %s, %s, %s, now(), now())"
        cursor.execute(sql, (nom, prenom, sexe, date, autre, traitement))
        connection.commit()
    else:
        sql = "INSERT INTO TIPE.PATIENTS (Nom, Prenom, Sexe,  Autre, Traitement, Date_creat, Date_der_modif)"\
              +"values (%s, %s, %s, %s, %s, now(), now())"
        cursor.execute(sql, (nom, prenom, sexe, autre, traitement))
        connection.commit()
    print("Création éffectué")
        
def baseListPat(listbox): # Récupération des différents patients
    global connection
    cursor = connection.cursor()
    sql = "SELECT idPATIENTS, Nom, Prenom FROM TIPE.PATIENTS"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in range(len(results)):
        listbox.insert(i, str(results[i][0])+" "+str(results[i][1])+" "+str(results[i][2]))
    connection.commit()
def baseNomPat(Id): # Récupère le nom et le prénom du patient par l'Id
    global connection
    cursor = connection.cursor()
    sql = "SELECT Nom, Prenom FROM TIPE.PATIENTS WHERE idPATIENTS = " + str(Id)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results[0][0] + " " + results[0][1]

def baseDonPat(Id): # Récupération des infos d'un patients demandé par Id
    global connection
    cursor = connection.cursor()
    sql = "SELECT * FROM TIPE.PATIENTS WHERE idPATIENTS = "+ str(Id)
    cursor.execute(sql)
    results = cursor.fetchall()
    if results[0][4] != None:
        date_nais = '{:%Y%m%d}'.format(results[0][4])
    else:
        date_nais = ""
    result = [results[0][1], results[0][2], results[0][3], date_nais, results[0][5], results[0][6]]
    #result = ['Nom', 'Prénom', 'Sexe', 'Date de naissance', 'autre', 'traitement']
    connection.commit()
    return result
    
def baseModifPat(Id, prenom, nom, sexe, date, autre, traitement, valid):
    global connection
    cursor = connection.cursor()
    result = baseDonPat(Id)
    text = ""
    if nom != result[0]:
        text+= "Nom = '" + ecrit(nom) + "'"
    if prenom != result[1]:
        text += virgule(text, ' , ') + "Prenom = '" + str(prenom) + "'"
    if sexe != result[2]:
        text += virgule(text, ' , ') + "Sexe = '" + str(sexe) + "'"
    if date != result[3] and valid:
        text += virgule(text, ' , ') + "Date_nais = '" + str(date) + "'"
    if autre != result[4]:
        text += virgule(text, ' , ') + "Autre = '" + str(autre) + "'"
    if traitement != result[5]:
        text += virgule(text, ' , ') + "Traitement = '" + str(traitement) + "'"

    if text != "":
        text += ", Date_der_modif = now()"
        sql = "UPDATE TIPE.PATIENTS SET {} WHERE idPATIENTS = {};".format(text, Id)
        cursor.execute(sql)
        connection.commit()
        print("Modification éffectué")

def baseDemandDon(Id, time, type_prise):
    global connection
    cursor = connection.cursor()
    t_type_prise =""
    for i in range (len(type_prise)):
        t_type_prise += virgule(t_type_prise, " OR ") + "idTYPE_PRISE = "+ str(type_prise[i])
    sql = "SELECT idTYPE_PRISE, Date_prise, Valeur_prise FROM tipe.valeurs WHERE idPATIENTS = {} AND Date_prise >= DATE_SUB(NOW(), INTERVAL {} HOUR) AND ({});".format(str(Id), str(time), t_type_prise)
    cursor.execute(sql)
    results = cursor.fetchall()
    connection.commit()
    nom = baseNomPat(Id)
    exploit_donne(Id, time, type_prise, results, nom)
    return True
