import pymysql.cursors
from random import *
import time

connection = pymysql.connect (host = 'localhost',
                              user = 'python',
                              password = '86.07')

for i in range (100):
    idPATIENTS = 9
    idTYPE_PRISE = randint(1, 5)
    if idTYPE_PRISE == 1:
        Valeur_prise = randint(50, 150)
    elif idTYPE_PRISE == 2:
        Valeur_prise = uniform(6, 11) # entre 6 et 11
    elif idTYPE_PRISE == 3:
        Valeur_prise = uniform(10, 20) # entre 10 et 20
    elif idTYPE_PRISE == 4:
        Valeur_prise = randint(85, 100)
    elif idTYPE_PRISE == 5:
        Valeur_prise = uniform(35, 39) # entre 35 et 39
    print(i, "/ \ti = ", idPATIENTS, " , idType_prise = ", idTYPE_PRISE, " , idPatients = ", idPATIENTS, " , Valeur_prise = ", Valeur_prise)
    sql = "INSERT INTO TIPE.VALEURS (idPatients, idType_prise, Date_prise, Valeur_prise) VALUES ( {}, {}, now(), {});".format(idPATIENTS, idTYPE_PRISE, Valeur_prise)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    time.sleep(1)
