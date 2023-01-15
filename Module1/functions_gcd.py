# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:07:55 2022

@author: abilash
"""

##Function arguments example 2
##

def gcd(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd

def lcm(x,y):
    return((x*y)//gcd(x,y))

print("Enter numbers for finding GCD:")
print("Enter first number:")
a = int(input())
print("Enter second number:")
b = int(input())
 
# prints 12
print ("The gcd of ",a,"and ",b," is : ", end="")
print (gcd(a,b))

print ("The lcm of ",a,"and ",b," is : ", end="")
print (lcm(a,b))
