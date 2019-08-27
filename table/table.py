# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: table.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

def table(nb, max):

    i = 0

    while i < max:
        i += 1
        print(i, "*", nb, "=", i * nb)

table(12, 20)
