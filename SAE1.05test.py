import numpy as np
import datetime
import os
import csv
import typing
import matplotlib.pyplot as plt
import pylab

try:
    with open("DumpFile.txt", encoding="utf8") as fh:
        res = fh.read()
except:
    print("Le fichier n'existe pas %s", os.path.abspath('DumpFile.txt'))
ress = res.split('\n')
tab_dest = np.array([])
tableau_evenements = np.array([])
fic = open("Tableau.csv", "w")  # Tableau est le fichier d'arrivée des extractions
evenement = "DATE ; SOURCE ; PORT ; DESTINATION ; FLAG ; SEQ ; ACK ; WIN ; OPTIONS ; LENGTH"  # intitulé de mes colonnes
fic.write(evenement + "\n")  # écriture de mes titres dans le tableur
characters = ":"  # définir une variable avec le caractère ":" (qui nous sera utile pour la suite)
for event in ress:
    if event.startswith('11:42'):  # évenement qui commence par "11:42" (ils commencent tous par 11:42)
        # déclaration variables et remise à zéro
        seq = ""
        heure1 = ""
        nomip = ""
        port = ""
        flag = ""
        ack = ""
        win = ""
        options = ""
        length = ""
        # Pour la date de l'évenement (première colonne)
        texte = event.split(" ")
        heure1 = texte[0]

        # Pour la source (2ème colonne)
        texte = event.split(" ")
        source = texte[2]

        # Pour le port (3ème colonne)
        port1 = texte[2].split(".")
        port = port1[-1]

        # Pour la destination (4ème colonne)
        texte = event.split(" ")
        destination = texte[4]

        # Flag (5ème colonne)
        texte = event.split("[")  # On coupe à partir du crochet
        if len(texte) > 1:  # s'il y a plus de une partie à partir du crochet
            flag1 = texte[1].split("]")  # on prend après le premier crochet et on coupe au deuxième crochet
            flag = flag1[0]  # pourquoi 0 ? Car on prend la partie de gauche du deuxième crochet (ce qu'on recherche)

            # seq (6ème colonne)
            seq = texte[1].strip()
            # ACK (7ème colonne)
            texte = event.split("ack")
            ack = texte[1].strip()
            # WIN (8ème colonne)
            texte = event.split("win")
            win = texte[1].strip()
            # OPTIONS (9ème colonne)
            texte = event.split("options")
            options = texte[1].strip()
            # LENGTH (10ème colonne)
            texte = event.split("length")
            length = texte[1].strip()

            # Ecriture dans le fichier csv
            fic.write(heure1 + " ; " + source + " ; " + port + " ; " + destination + " ; " + flag + " ; " + seq + " ; " + ack + " ; " + win + " ; " + options + " ; " + length + "\n")