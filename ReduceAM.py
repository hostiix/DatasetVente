import sys
import random
from typing import TextIO
import datetime
import re
import os
from math import *

# Exécution du script : Ouvrir terminal, exécuter si Windows: "type file.csv | python mapper.py | python reduce.py"
#type data.csv | C:\Users\silva\AppData\Local\Programs\Python\Python37\python.exe TestMapper.py | C:\Users\silva\AppData\Local\Programs\Python\Python37\python.exe TestReduce.py

file: TextIO = open("FichierMock_modif.csv", "w")
file.write(
    '%s;%s;%s;%s;%s;%s;%s\n' % (
        "id_vente", "date_vente", "id_client", "id_magasin", "prix_vente_unitaire", "quantité", "id_produit"))

jours_ferié_fermé = ["01/01", "01/05", "25/12"]
jours_ferié_ouvert = ["08/05", "15/08", "14/07", "01/11", "11/11"]

# Nombre de produit dans la commande
nb_product_invoice_random = random.randint(1, 10)
# Nombre d'article dans la commande dans la boucle
nb_product_invoice = 1

# Nombre de vente par jours
#nb_vente_jours = 30000

# Nombre servant pour les id
id_vente = 1
id_client = random.randint(1, 98758)
id_magasin = random.randint(1,250)
id_produit = random.randint(1,1000000)

#Partitioner
for line in sys.stdin:
    line = line.strip()
    line = line.split(";")

    jour_de_la_semaine = line[0]
    annee = line[1]
    mois = int(line[2]) + 1
    mois = str(mois)
    jour_du_mois = line[3]

    date = str(jour_du_mois) + "/" + mois + "/" + str(annee)

    nb_vente_jours = 30000

    #Lundi
    if jour_de_la_semaine == 1 :
        nb_vente_jours = nb_vente_jours*0,8
    #Mardi
    elif jour_de_la_semaine == 2:
        nb_vente_jours = nb_vente_jours*0,7
    #Mercredi, vendredi ou dimanche
    elif jour_de_la_semaine == 3 or jour_de_la_semaine ==5 or jour_de_la_semaine == 7 :
        nb_vente_jours = nb_vente_jours*1.2
    #Jeudi
    elif jour_de_la_semaine == 4:
        nb_vente_jours = nb_vente_jours*1
    #Samedi
    elif jour_de_la_semaine == 6:
        nb_vente_jours = nb_vente_jours*1.6

    #Janvier
    if mois == 1 :
        nb_vente_jours = nb_vente_jours*1.5
    #Fevrier ou Octobre
    elif mois == 2 or mois == 10 :
        nb_vente_jours = nb_vente_jours*1
    #Mars ou Avril
    elif mois == 3 or mois == 4 :
        nb_vente_jours = nb_vente_jours*0.8
    #Mai ou Juin ou Septembre
    elif mois == 5 or mois == 6 or mois == 9 :
        nb_vente_jours = nb_vente_jours*1.2
    #Juillet ou Aout
    elif mois == 7 or mois == 8 :
        nb_vente_jours = nb_vente_jours*0.7
    #Novembre
    elif mois == 11 :
        nb_vente_jours = nb_vente_jours*1.3
    #Decembre
    elif mois == 12 :
        nb_vente_jours = nb_vente_jours*1.8

    for i in range (1, floor(nb_vente_jours)) :
        if nb_product_invoice <= nb_product_invoice_random :
            nb_product_invoice = nb_product_invoice + 1
        else :
            id_vente = id_vente + 1
            id_client = random.randint(1, 98758)
            id_magasin = random.randint(1, 250)
            id_produit = random.randint(1, 1000000)
            nb_product_invoice = 1
            nb_product_invoice_random = random.randint(1,10)

        prix = round(random.uniform(0.7, 50.00), 2)
        quantite = random.randint(1,10)

        file.write(
            '%s;%s;%s;%s;%s;%s;%s\n' % (
                id_vente, date, id_client, id_magasin, prix, quantite, id_produit))


"""

# Initialisation d'un numéro d'id random, et d'une date
id_invoice_temp = str(random.randint(0, 99))
invoice_year = str(random.randint(2017,2019))
invoice_month = str(random.randint(1,12))
invoice_day = str(random.randint(1, 29))
invoice_hour = str(random.randint(9, 22))
invoice_minute = str(random.randint(0, 59))

# Partitioner
for line in sys.stdin:
    # line = line.strip()
    line = line.split(",")

    # Vérification du nombre d'article dans la commande
    if nb_product_invoice <= nb_product_invoice_random:
        nb_product_invoice = nb_product_invoice + 1
    else:
        # Nouvelle commande -> Nouvel id, reinit du nb d'article, nouvelle date
        id_invoice_temp = line[0]
        id_invoice_random = str(random.randint(0, 10000))
        nb_product_invoice = 1
        invoice_year = line[2]
        invoice_month = line[3]
        invoice_day = str(random.randint(1, 29))
        invoice_hour = str(random.randint(9, 22))
        invoice_minute = str(random.randint(0, 59))

    id_invoice = id_invoice_temp + id_invoice_random

    quantity_line1 = int(line[1])

    # Transformation sur les quantités, afin d'avoir des quantités cohérentes
    if quantity_line1 > 10 and quantity_line1 <= 100:
        quantity = quantity_line1 % 10
    elif quantity_line1 > 100 and quantity_line1 <= 1000:
        quantity = quantity_line1 % 100
    elif quantity_line1 > 1000 and quantity_line1 <= 10000:
        quantity = quantity_line1 % 1000
    elif quantity_line1 > 1000 and quantity_line1 <= 100000:
        quantity = quantity_line1 % 10000
    elif quantity_line1 < 0:
        quantity = random.randint(-7, -1)
    else:
        quantity = quantity_line1

    invoice_date = invoice_day + "/" + invoice_month + "/" + invoice_year + " " + invoice_hour + ":" + invoice_minute + ":00"

    product_unit_price_line4 = float(line[4])

    if product_unit_price_line4 > 30 :
        product_unit_price = round(random.uniform(0.8, 30), 3);
    elif product_unit_price_line4 < 0:
        product_unit_price = round(random.uniform(-2, 30),3);
    else :
        product_unit_price = product_unit_price_line4

    file.write('%s;%s;%s;%s\n' % (
        id_invoice, quantity, invoice_date, product_unit_price))
"""
file.close()
