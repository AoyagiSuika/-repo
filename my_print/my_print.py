#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: my_print.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

def my_print(*parametres, sep=' ', end='\n'):
    parametres = list(parametres)

    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)

    res = sep.join(parametres)
    res += end

    print(res, end='')
