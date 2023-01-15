# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:47:59 2022

@author: abilash
"""
print('Lets Print the Fibonacee Series.')
nterm = int(input('Enter the number of terms to print..!!!'))
n1 = 0
n2 = 1
print("Term 1 is ",n1)
print("Term 2 is ",n2)
for i in range(3,nterm+1):
    temp = n1
    n1 = n2
    n2 = n1 + temp
    print("Term",i," is ",n2)
    