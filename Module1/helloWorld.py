# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:15:44 2022

@author: abilash

functions:

    print() - display output on console
    input() - accept STRING (only) from console
    len() - displays the length of a string (num of charecters)
    str() - converting "any data type" to string
    int() - convert integer numerals in a str type to int type

"""
#%% Accept Name
print('Hello world!') 
print('What is your name?')
myName = input() 

#%% Calculate and Print length of name
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

#%%Accept age and print age after 1 year
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')