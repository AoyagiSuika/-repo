#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: table.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

"""module mult contenant la fonction table"""

def table(nb, max = 10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb

    (max >= 0)"""

    i = 0

    while i < max:
        i += 1
        print(i, "*", nb, "=", i * nb)

if __name__ == "__main__":
    table(4)
    input("Appuyez sur ENTREE pour fermer le programme...")
