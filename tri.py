import os

#command = "mv c:/Users/Alex/Desktop/Tri/" +variable +" c:/Users/Alex/Desktop/Tri/dossier"
#print(command)
#os.system(command)

cmd_output = os.listdir("C:/Users/Alex/Desktop/Tri/")
#print(cmd_output)

film = "avi"
texte = "txt"
libreoffice = "odp"

#commande_film = "mv c:/Users/Alex/Desktop/Tri/" +item +" c:/Users/Alex/Desktop/Tri/dossier_film/"
#commande_texte = "mv c:/Users/Alex/Desktop/Tri/" +item +" c:/Users/Alex/Desktop/Tri/dossier_texte/"
#commande_odp = "mv c:/Users/Alex/Desktop/Tri/" +item +" c:/Users/Alex/Desktop/Tri/dossier_libreoffice/"


for item in cmd_output:
    #Tri des fichiers avi
    if item.count(film) >= 1:
        print("film trouvé")
        i = item
        os.system("mv c:/Users/Alex/Desktop/Tri/" +i +" c:/Users/Alex/Desktop/Tri/dossier_film/")
    #Tri des fichiers txt
    elif item.count(texte) >= 1:
        print("fichier texte trouvé")
        i = item
        os.system("mv c:/Users/Alex/Desktop/Tri/" +i +" c:/Users/Alex/Desktop/Tri/dossier_texte/")
    #Tri des fichiers odp
    elif item.count(libreoffice) >= 1:
        print("fichier libreoffice trouvé")
        i = item
        os.system("mv c:/Users/Alex/Desktop/Tri/" +i +" c:/Users/Alex/Desktop/Tri/dossier_libreoffice/")



