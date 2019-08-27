#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: comprehensions.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

inv = [
    ("melons", 4),
    ("prunes", 51),
    ("poires", 18),
    ("fraises", 76),
    ("pommes", 22),
]

tmp = [(qtt, fruit) for fruit, qtt in inv]

tmp.sort(reverse=True)

inv = [(fruit, qtt) for qtt, fruit in tmp]
