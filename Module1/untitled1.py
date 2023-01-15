# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:20:23 2022

@author: abilash
"""

def spam():
    global eggs
    print("Before changing...",eggs)
    eggs = 'spam'
    print("After changing...",eggs)

eggs = 'gun'
spam()
print(eggs)