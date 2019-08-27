#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: aff_float.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

def aff_float(nb):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères
    représentant la troncature de ce nombre. La partie flottante doit avoir une longueur
    maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""

    if type(nb) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    nb = str(nb)
    ent, flo = nb.split(".")
    return ",".join([ent, flo[:3]])
