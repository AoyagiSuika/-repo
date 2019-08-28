#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: ZCasino.py
# @Last modified by:   suika
# @Last modified time: 28-08-2019

from random import randrange
from math import ceil
import pickle

def regles():
    """Fonction rappelant les règles de la roulette"""

    print("Voici les règles :")
    print("Vous misez sur un nombre compris entre 0 et 49.")
    print("Si la bille tombe sur votre nombre, vous récupérez")
    print("trois fois votre mise. Sinon, si la bille tombe sur")
    print("une case de la même couleur que votre nombre, vous")
    print("récupérez la moitié de votre mise. Sinon, c'est perdu.\n")

def roulette(nb, mise, argent):
    """Fonction jouant le rôle de la roulette"""

    res = randrange(50)
    if res == nb:
        print("Félicitations, vous avez misé sur le bon nombre !")
        print("Vous remportez", 3 * mise, "$ !")
        argent = argent + (3 * mise)
        return argent
    elif res % 2 == nb % 2:
        print("Vous aviez la bonne couleur, vous récupérez", ceil(mise / 2),\
        "$, ce n'est pas si mal !")
        argent = argent + (ceil(mise / 2))
        return argent
    else:
        print("Perdu !")
        return argent

continuer = True

with open("argent", "r") as fichier:
    argent = fichier.read()
    argent = int(argent)

print("Bienvenue au ZCasino !")
regles()
while continuer == True and argent > 0:
    print("Vous disposez de", argent, "$.\n")
    nb = input("Sur quel nombre voulez-vous miser ?\n")
    try:
        nb = int(nb)
        if not (nb >= 0 and nb <= 49):
            raise ValueError("Le nombre doit être compris entre 0 et 49.")
    except ValueError as error:
        print(error)
        continue
    except TypeError:
        print("Veuillez entrer un nombre entre 0 et 49.")
        continue
    else:
        mise = input("Combien souhaitez-vous miser ?\n")
        try:
            mise = int(mise)
            if mise < 5:
                raise ValueError("Votre mise doit être d'au moins 5$.")
            if mise > argent:
                print("Vous n'avez pas autant d'argent.")
                continue
        except ValueError as error:
            print(error)
            continue
        except TypeError:
            print("Veuillez entrer un nombre valide.")
            continue
        else:
            print("\nVous avez misé", mise, "$ sur le", nb,\
            "lançons la roulette !\n")
            argent = argent - mise
            argent = roulette(nb, mise, argent)
    finally:
        if argent > 0:
            print("Il vous reste", argent, "$.")
            with open("argent", "w") as fichier:
                argent = str(argent)
                fichier.write(argent)
                argent = int(argent)
            rep = input("Souhaitez-vous rejouer ? Y/N\n")
            if rep == "Y" or rep == "y":
                print("C'est reparti !")
            else:
                print("Au revoir !")
                continuer = False
        else:
            print("Vous êtes ruiné. Au revoir !")
            with open("argent", "w") as fichier:
                fichier.write("1000")
            continuer = False
