# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:24:06 2022

@author: abilash
"""

##function to add two numbers
def disp_sum(a,b):
    #print("The sum of ",a,"and ",b,"is ")
    print(a+b)
    return None

##Get numbers to be added
print("Enter Two numbers to add:")
print("Enter first number:")
a = int(input())
print("Enter second number:")
b = int(input())

##Call function to add and display sum
s = disp_sum(a,b)
d = print(s)
print(d)