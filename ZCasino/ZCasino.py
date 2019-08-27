#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: ZCasino.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

from random import randrange
from math import ceil

def regles():
    """Fonction rappelant les règles de la roulette"""

    print("Voici les règles :")
    print("Vous misez sur un nombre compris entre 0 et 49.")
    print("Si la bille tombe sur votre nombre, vous récupérez")
    print("trois fois votre mise. Sinon, si la bille tombe sur")
    print("une case de la même couleur que votre nombre, vous")
    print("récupérez la moitié de votre mise. Sinon, c'est perdu.")

def roulette(nb, mise):
    """Fonction jouant le rôle de la roulette"""

    res = randrange(50)
    if res == nb:
        print("Félicitations, vous avez misé sur le bon nombre !")
        print("Vous remportez", 3 * mise, "$ !")
    elif res % 2 == nb % 2:
        print("Vous aviez la bonne couleur, vous récupérez", ceil(mise / 2),\
        "$, ce n'est pas si mal !")
    else:
        print("Perdu !")

print("Bienvenue au ZCasino !")
regles()
nb = input("Sur quel nombre voulez-vous miser ?\n")
try:
    nb = int(nb)
    if not (nb >= 0 and nb <= 49):
        raise ValueError("Le nombre doit être compris entre 0 et 49.")
except ValueError as error:
    print(error)
except TypeError:
    print("Veuillez entrer un nombre entre 0 et 49.")
else:
    mise = input("Combien souhaitez-vous miser ?\n")
    try:
        mise = int(mise)
        if mise < 5:
            raise ValueError("Votre mise doit être d'au moins 5$.")
    except ValueError as error:
        print(error)
    except TypeError:
        print("Veuillez entrer un nombre valide.")
    else:
        print("Vous avez misé", mise, "$ sur le", nb,\
        "lançons la roulette !")
        roulette(nb, mise)
