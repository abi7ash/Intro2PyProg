# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:52:01 2022

@author: abilash
"""

def spam():
    global eggs
    eggs = 'spam-eggs' # this is the global

def bacon():
    eggs = 'bacon-eggs' # this is a local
    print("inside bacon, eggs is: ",eggs) # this is the global

def ham():
    print("inside ham, eggs is: ",eggs) # this is the global
 
eggs = 42 # this is the global
print('Eggs initially = ',eggs)
spam()
print("After spam() eggs is:",eggs)
bacon()
print("After bacon() eggs is:",eggs)
ham()
print("After ham() eggs is:",eggs)
