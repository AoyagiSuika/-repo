# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: bissextile.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

annee = input("Saisissez une année : ")
annee = int(annee)

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print(annee, "est une année bissextile.")
else:
    print(annee, "n'est pas une année bissextile.")
