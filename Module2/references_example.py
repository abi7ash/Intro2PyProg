# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:36:07 2022

@author: abilash
"""
#%% Example for reference in lists
spam = [0, 1, 2, 3, 4, 5]
print('Before mod')
print('spam =',spam)
#print('cheese =',cheese)
cheese = spam
cheese[1] = 'Hello!'
print('spam =',spam)
print('cheese =',cheese)

#%% Passing refernces in a function

def eggs(someParameter):
 someParameter.append('Hello')
 
spam = [1, 2, 3]
print('spam before eggs:',spam)
eggs(spam)
print('spam after eggs:',spam)

#%%