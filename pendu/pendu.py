#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   28-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: pendu.py
# @Last modified by:   suika
# @Last modified time: 28-08-2019

import fonctions
import donnees

scores = fonctions.get_scores(donnees.scores)
name, score = fonctions.get_name(donnees.name, scores, donnees.score)
print("score :", score)
print(name)

while donnees.continuer == True:
    mot = fonctions.pick_word(donnees.mots, donnees.mot)
    fonctions.pendu(mot, name, score, scores)
    c = input("Voulez-vous rejouer ? Y/N\n")
    if c in "yY":
        continue
    else:
        donnees.continuer = False
        print("Au revoir !")
