# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:10:46 2022

@author: abilash
"""
#%%Function for Factorial
def factorial(n):
    if(n == 0):
        return(1)
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return(fact)

#%% To test factorial
print("Enter value for n:")
n=int(input())
print("factorial for ",n," is:",factorial(n))

#%% To compute binomial coefficient
print("Enter the values for n and r for nCr!!")
print("Enter n:")
n = int(input())
print("Enter r:")
r = int(input())
ncr=int(factorial(n)/(factorial(n-r)*factorial(r)))
print("Coefficient for nCr is:",ncr)