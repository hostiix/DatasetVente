import sys
import random
from typing import TextIO
import datetime
import re
import os
from math import *

# Exécution du script : Ouvrir terminal, exécuter si Windows: "type file.csv | python mapper.py | python reduce.py"
# type data.csv | C:\Users\silva\AppData\Local\Programs\Python\Python37\python.exe TestMapper.py | C:\Users\silva\AppData\Local\Programs\Python\Python37\python.exe TestReduce.py

file: TextIO = open("FichierMock_modif2.csv", "w")
file.write(
    '%s;%s;%s;%s;%s;%s;%s\n' % (
        "id_vente", "date_vente", "id_client", "id_magasin", "prix_vente_unitaire", "quantité", "id_produit"))

jours_ferié_fermé = ["1/1", "1/5", "25/12"]
jours_ferié_ouvert = ["8/5", "15/8", "14/7", "1/11", "11/11"]

# Nombre de produit dans la commande
nb_product_invoice_random = random.randint(1, 10)
# Nombre d'article dans la commande dans la boucle
nb_product_invoice = 1

# Nombre de vente par jours
# nb_vente_jours = 30000

# Nombre servant pour les id
id_vente = 1
id_client = random.randint(1, 98758)
id_magasin = random.randint(1, 250)
id_produit = random.randint(1, 1000000)

# Partitioner
for line in sys.stdin:
    line = line.strip()
    line = line.split(";")

    nb_vente_jours = 50000.0

    jour_de_la_semaine = int(line[0])
    annee = line[1]
    mois = int(line[2]) + 1
    mois_str = str(mois)
    jour_du_mois = line[3]

    date_jours_mois = str(jour_du_mois) + "/" + mois_str

    if date_jours_mois in jours_ferié_fermé:
        print("jours ferié fermé")
        nb_vente_jours = nb_vente_jours * 0
    elif date_jours_mois in jours_ferié_ouvert:
        print("jours ferié ouvert")
        nb_vente_jours = nb_vente_jours * 1.4

    date = str(jour_du_mois) + "/" + mois_str + "/" + str(annee)

    # Lundi
    if jour_de_la_semaine == 1:
        nb_vente_jours = nb_vente_jours * 0.8
    # Mardi
    elif jour_de_la_semaine == 2:
        nb_vente_jours = nb_vente_jours * 0.7
    # Mercredi, vendredi ou dimanche
    elif jour_de_la_semaine == 3 or jour_de_la_semaine == 5 or jour_de_la_semaine == 7:
        nb_vente_jours = nb_vente_jours * 1.2
    # Jeudi
    elif jour_de_la_semaine == 4:
        nb_vente_jours = nb_vente_jours * 1
    # Samedi
    elif jour_de_la_semaine == 6:
        nb_vente_jours = nb_vente_jours * 1.6

    # Janvier
    if mois == 1:
        nb_vente_jours = nb_vente_jours * 1.5
    # Fevrier ou Octobre
    elif mois == 2 or mois == 10:
        nb_vente_jours = nb_vente_jours * 1
    # Mars ou Avril
    elif mois == 3 or mois == 4:
        nb_vente_jours = nb_vente_jours * 0.8
    # Mai ou Juin ou Septembre
    elif mois == 5 or mois == 6 or mois == 9:
        nb_vente_jours = nb_vente_jours * 1.2
    # Juillet ou Aout
    elif mois == 7 or mois == 8:
        nb_vente_jours = nb_vente_jours * 0.7
    # Novembre
    elif mois == 11:
        nb_vente_jours = nb_vente_jours * 1.3
    # Decembre
    elif mois == 12:
        nb_vente_jours = nb_vente_jours * 1.8

    for i in range(1, floor(nb_vente_jours)):
        if nb_product_invoice <= nb_product_invoice_random:
            nb_product_invoice = nb_product_invoice + 1
        else:
            id_vente = id_vente + 1
            id_client = random.randint(1, 98758)
            id_magasin = random.randint(1, 250)
            nb_product_invoice = 1
            nb_product_invoice_random = random.randint(1, 10)

        id_produit = random.randint(1, 1000000)
        prix = round(random.uniform(0.7, 50.00), 2)
        quantite = random.randint(1, 10)

        file.write(
            '%s;%s;%s;%s;%s;%s;%s\n' % (
                id_vente, date, id_client, id_magasin, prix, quantite, id_produit))

file.close()
