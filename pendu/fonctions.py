#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   28-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: fonctions.py
# @Last modified by:   suika
# @Last modified time: 28-08-2019

from random import randrange
import os.path
import donnees
import pickle
import json

def get_scores(scores):
    """Fonction récupérant les scores dans le fichier
    scores"""

    if os.path.isfile("scores"):
        with open("scores", "rb") as fichier:
            depickler = pickle.Unpickler(fichier)
            scores = depickler.load()
            print("Tableau des scores :")
            print(scores, "\n")
    else:
        with open("scores", "xb") as fichier:
            scores = {}
            pickler = pickle.Pickler(fichier)
            pickler.dump(scores)
    return scores

def get_name(name, scores, score):
    """Fonction récupérant le nom de l'utilisateur
    et le score associé s'il y en a un"""

    name = input("Veuillez entrer votre nom : ")
    if not name.isalnum() or len(name) < 1:
        print("Veuillez entre un nom valide.")
        return get_name(name, scores, score)
    if name in scores:
        score = scores[name]
        print("Votre score actuel est de", score)
    else:
        scores[name] = name, 0
        print("Votre score actuel est de", score)
    return name, score

def pick_word(mots, mot):
    """Fonction choisissant un mot au hasard dans la
    liste"""

    mot = mots[randrange(donnees.nb_mots)]
    return mot

def update_score(name, scores, score):
    """Fonction mettant à jour le score du joueur"""

    scores[name] = score
    with open("scores", "wb") as fichier:
        pickler = pickle.Pickler(fichier)
        pickler.dump(scores)

def pendu(mot, name, score, scores):
    """Le jeu du pendu"""

    res = "*****"
    win = 1
    print(res)

    while res != mot and donnees.nb_chances > 0:
        i = 0
        print("Il vous reste", donnees.nb_chances, "essais.")
        lettre = input("Entrez une lettre : ")
        lettre = lettre.lower()
        if len(lettre) > 1 or not lettre.isalpha():
            print("Vous devez entrer une lettre.")
            continue
        if lettre in donnees.found:
            print("Vous avez déjà essayé cette lettre.")
            continue
        if lettre in mot:
            donnees.found.append(lettre)
            res = ""
            for char in mot:
                if char in donnees.found:
                    res += char
                else:
                    res += "*"
        else:
            donnees.nb_chances -= 1
        print(res)
    if res == mot:
        print("Félicitations, vous avez gagné !")
        score += donnees.nb_chances
        print("Votre score actuel est de", score)
    else:
        print("Perdu !")
        print("Votre score actuel est de", score)
    update_score(name, scores, score)
