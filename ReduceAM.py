import sys
import random
from typing import TextIO
import datetime
import re
import os
from math import *

# Exécution du script : Ouvrir terminal, exécuter si Windows: "type file.csv | python mapper.py | python reduce.py"
# type DateUnique.csv | C:\Users\silva\AppData\Local\Programs\Python\Python37\python.exe ReduceAM.py

file: TextIO = open("FichierMock_modif4.csv", "w")
file.write(
    '%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
        "id_vente", "date_vente", "id_client", "categorie_client","id_magasin", "prix_vente_unitaire", "quantité", "id_produit", "categorie_produit"))

jours_ferié_fermé = ["1/1", "1/5", "25/12"]
jours_ferié_ouvert = ["8/5", "15/8", "14/7", "1/11", "11/11"]

#Les catégories des clients / Produits
categorie = ["High-tech", "Sport", "Bio", "Nourriture", "Mode", "Jardinage", "Multimédia", "Culturel", "Enfant", "Beauté/bijoux", "Autre"]

# Nombre de produit dans la commande
nb_product_invoice_random = random.randint(1, 10)
# Nombre d'article dans la commande dans la boucle
nb_product_invoice = 1


# Nombre servant pour les id
id_vente = 1
id_client = random.randint(1, 98758)
# Affectation de la catégorie du profil client
if id_client >= 1 and id_client < 15001:
    categorie_client = categorie[0]  # Profil High-Tech

elif id_client > 15002 and id_client < 30003:
    categorie_client = categorie[1]  # Profil Sport

elif id_client > 30004 and id_client < 36463:
    categorie_client = categorie[2]  # Profil Bio

elif id_client > 36464 and id_client < 51465:
    categorie_client = categorie[3]  # Profil Nourriture

elif id_client > 51466 and id_client < 67467:
    categorie_client = categorie[4]  # Profil Mode

elif id_client > 67468 and id_client < 74927:
    categorie_client = categorie[5]  # Profil Jardinage

elif id_client > 74928 and id_client < 82387:
    categorie_client = categorie[6]  # Profil Multimédia

elif id_client >82388 and id_client < 90847:
    categorie_client = categorie[7]  # Profil Culturel

elif id_client > 90848 and id_client < 97307:
    categorie_client = categorie[8]  # Profil Enfant

elif id_client > 97308 and id_client < 98667:
    categorie_client = categorie[9]  # Profil Beauté/Bijoux

elif id_client > 98668 and id_client < 98767:
    categorie_client = categorie[10] # Profil Autre

id_magasin = random.randint(1, 250)
id_produit = random.randint(1, 100000)

# Partitioner
for line in sys.stdin:
    line = line.strip()
    line = line.split(";")

    # Nombre de vente par jours
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

            #Affectation de la catégorie du profil client
            if id_client >= 1 and id_client < 15001:
                categorie_client = categorie[0]  # Profil High-Tech

            elif id_client > 15002 and id_client < 30003:
                categorie_client = categorie[1]  # Profil Sport

            elif id_client > 30004 and id_client < 36463:
                categorie_client = categorie[2]  # Profil Bio

            elif id_client > 36464 and id_client < 51465:
                categorie_client = categorie[3]  # Profil Nourriture

            elif id_client > 51466 and id_client < 67467:
                categorie_client = categorie[4]  # Profil Mode

            elif id_client > 67468 and id_client < 74927:
                categorie_client = categorie[5]  # Profil Jardinage

            elif id_client > 74928 and id_client < 82387:
                categorie_client = categorie[6]  # Profil Multimédia

            elif id_client > 82388 and id_client < 90847:
                categorie_client = categorie[7]  # Profil Culturel

            elif id_client > 90848 and id_client < 97307:
                categorie_client = categorie[8]  # Profil Enfant

            elif id_client > 97308 and id_client < 98667:
                categorie_client = categorie[9]  # Profil Beauté/Bijoux

            elif id_client > 98668 and id_client < 98767:
                categorie_client = categorie[10]  # Profil Autre

            id_magasin = random.randint(1, 250)
            nb_product_invoice = 1
            nb_product_invoice_random = random.randint(1, 10)

        proba_produit_achete_profil = random.randint(1,100)
        proba_borne_random = random.randint(1,2)

        if proba_produit_achete_profil < 76: #Dans 75% des cas le client achete des produits similaire à son profil
            if categorie_client == categorie[0]: # Profil High-Tech
                id_produit = random.randint(1,15000)

            elif categorie_client == categorie[1]: # Profil Sport
                id_produit = random.randint(15001, 30000)

            elif categorie_client == categorie[2]: # Profil Bio
                id_produit = random.randint(30001, 36668)

            elif categorie_client == categorie[3]: # Profil Nourriture
                id_produit = random.randint(36669, 51669)

            elif categorie_client == categorie[4]: # Profil Mode
                id_produit = random.randint(51670, 66670)

            elif categorie_client == categorie[5]: # Profil Jardinage
                id_produit = random.randint(66671, 73338)

            elif categorie_client == categorie[6]: # Profil Multimédia
                id_produit = random.randint(73339, 80006)

            elif categorie_client == categorie[7]: # Profil Culturel
                id_produit = random.randint(80007, 86674)

            elif categorie_client == categorie[8]: # Profil Enfant
                id_produit = random.randint(86675, 98942)

            elif categorie_client == categorie[9]: # Profil Beauté/Bijoux
                id_produit = random.randint(98843, 99900)

            elif categorie_client == categorie[10]: # Profil Autre
                id_produit = random.randint(99901,100000)

        else: #Dans les autres cas il achete des produits différents de son profils
            if categorie_client == categorie[0]: # Profil High-Tech
                id_produit = random.randint(15001,100000)

            elif categorie_client == categorie[1]: # Profil Sport
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 15000)
                else:
                    id_produit = random.randint(30001,100000)

            elif categorie_client == categorie[2]: # Profil Bio
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 30000)
                else:
                    id_produit = random.randint(36669, 100000)

            elif categorie_client == categorie[3]: # Profil Nourriture
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 36668)
                else:
                    id_produit = random.randint(51670, 100000)

            elif categorie_client == categorie[4]: # Profil Mode
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 51669)
                else:
                    id_produit = random.randint(66671, 100000)

            elif categorie_client == categorie[5]: # Profil Jardinage
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 66670)
                else:
                    id_produit = random.randint(73339, 100000)

            elif categorie_client == categorie[6]: # Profil Multimédia
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 73338)
                else:
                    id_produit = random.randint(80007, 100000)

            elif categorie_client == categorie[7]: # Profil Culturel
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 80006)
                else:
                    id_produit = random.randint(86675, 100000)

            elif categorie_client == categorie[8]: # Profil Enfant
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 86674)
                else:
                    id_produit = random.randint(98843, 100000)

            elif categorie_client == categorie[9]: # Profil Beauté/Bijoux
                if proba_borne_random == 1:
                    id_produit = random.randint(1, 98942)
                else:
                    id_produit = random.randint(99901, 100000)

            elif categorie_client == categorie[10]: # Profil Autre
                id_produit = random.randint(1,99900)


        #Affectation de la catégorie aux produits
        if id_produit >= 1 and id_produit < 15000:
            categorie_produit = categorie[0]  # Profil High-Tech

        elif id_produit > 15001 and id_produit < 30000:
            categorie_produit = categorie[1]  # Profil Sport

        elif id_produit > 30001 and id_produit < 36668:
            categorie_produit = categorie[2]  # Profil Bio

        elif id_produit > 36669 and id_produit < 51669:
            categorie_produit = categorie[3]  # Profil Nourriture

        elif id_produit > 51670 and id_produit < 66670:
            categorie_produit = categorie[4]  # Profil Mode

        elif id_produit > 66671 and id_produit < 73338:
            categorie_produit = categorie[5]  # Profil Jardinage

        elif id_produit > 73339 and id_produit < 80006:
            categorie_produit = categorie[6]  # Profil Multimédia

        elif id_produit > 80007 and id_produit < 86674:
            categorie_produit = categorie[7]  # Profil Culturel

        elif id_produit > 86675 and id_produit < 98942:
            categorie_produit = categorie[8]  # Profil Enfant

        elif id_produit > 98943 and id_produit < 99900:
            categorie_produit = categorie[9]  # Profil Beauté/Bijoux

        elif id_produit > 99901 and id_produit < 100000 :
            categorie_produit = categorie[10] # Profil Autre

        prix = round(random.uniform(0.7, 50.00), 2)
        quantite = random.randint(1, 10)

        file.write(
            '%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
                id_vente, date, id_client, categorie_client, id_magasin, prix, quantite, id_produit, categorie_produit))

file.close()
