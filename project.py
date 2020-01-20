import os
import subprocess

folder_path = "C:/Users/Alex/Desktop/Tri/"

test = os.listdir(folder_path)
print(type(test))


for i in test:
    print(i)

print("#----------------------#")

film = "avi"
texte = "txt"
office = "odp"

variable = "lol.non"
print(variable.count(film) or variable.count(texte) or variable.count(office))

variable = test[1]
print(type(variable))

subprocess.call(["mv" , folder_path ,variable, " C:/Users"])

