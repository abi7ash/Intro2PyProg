# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:13:56 2022

@author: abilash
"""

#%%The copy module 

import copy

#%% usage of copy module
spam = ['A', 'B', 'C', 'D']
cheese = spam
cheese.append('Ee')
print('spam after apppend:\n',spam)
print('cheese after append:\n',cheese)

cheese = copy.copy(spam)
cheese[1] = 42
print('spam after copy:\n',spam)
print('cheese after copy:\n',cheese)

#%% Without deppcopy
jam = ['a','A',12,['b',4,13.5]]
bread = copy.copy(jam)
print('jam is:',jam)
print('bread is:',bread)
print("bread[3][2] =",bread[3][2])
bread[3][2]=44
print("Changing bread[3][2]=44...now..")
print('jam is:',jam)
print('bread is:',bread)

#%% Using deepcopy
jam = ['a','A',12,['b',4,13.5]]
bread = copy.deepcopy(jam)
print('jam is:',jam)
print('bread is:',bread)
print("bread[3][2] =",bread[3][2])
bread[3][2]=44
print("Changing bread[3][2]=44...now..")
print('jam is:',jam)
print('bread is:',bread)


