import os
import sys

choix_nombre_dossier = int(input("Entrez le nombre de dossier que vous souhaitez créer : "))
for i in range(0,choix_nombre_dossier):
    nom = (input("nom du dossier a créer : "))
    for item in os.listdir("c:/Users/Alex/Desktop/dossier_test/"):
        if item == nom:
            print("le dossier existe deja")
            print("Fermeture du programme")
            sys.exit()


    os.makedirs("c:/Users/Alex/Desktop/dossier_test/" +nom)


























#if os.path.exists("C:/Users/Alex/Desktop/Tri/"):
#    print("le dossier existe")
#else:
#    print("le dossier n'existe pas")