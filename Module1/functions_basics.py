# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 08:55:44 2022

@author: abilash
"""

def a():
    print('Started a()')
    b()
    d()
    print('Ended a()')
    
def b():
    print('Started b()')
    c()
    print('Ended b()')
    
def c():
    print('Started c()')
    print('Ended c()')

def d():
    print('Started d()')
    print('Ended d()')
    
a()
    