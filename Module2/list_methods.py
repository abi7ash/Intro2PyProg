# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:01:32 2022

@author: abilash
"""

spam = ['hello', 'hi', 'howdy', 'heyas','hello']

#%% Usage of Index method

spam.index('hello')

spam.index('heyas')

#%% Usage of append Method
print(spam)
spam.append('welcome')
print(spam)

#%% Usage of insert Method
spam.insert(2,'zone')
print(spam)

#%% Usage of remove Method
spam.remove('heyas')
print(spam)

#%%
spam.remove('hello')
print(spam)

#%%Sorting of Values with sort() Method

spam = [2, 5, 3.14, 1, -7]
print(spam)
spam.sort()

print('\nAfter sorting:\n',spam)

#%%
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort()

print('\nAfter sorting:\n',spam)

#%% ASCIIbetical order
##spam = ['Ants', 'cats', 'Dogs', 'badgers', 'elephants']
spam = ['aAA', 'AAa', 'Aaa']
print(spam)
spam.sort()

print('\nAfter sorting:\n',spam)
 
#%% Force regular sorting
spam = ['Ants', 'cats', 'Dogs', 'badgers', 'elephants']
print(spam)
spam.sort(key=str.lower)

print('\nAfter sorting:\n',spam)
