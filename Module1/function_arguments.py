# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:33:20 2022

@author: abilash
"""

##Program to set grade from Marks

def marks2grade(marks):
    if marks >= 90:
        return 'O'
    elif marks >= 80:
        return 'A+'
    elif marks >= 70:
        return 'A'
    elif marks >= 60:
        return 'B+'
    elif marks >= 55:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'P'
    else:
        return 'F'

print('Enter marks out of 100')
marks_in = float(input())
marks2grade(marks_in)