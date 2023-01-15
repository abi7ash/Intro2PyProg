# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:16:15 2023

@author: abilash
"""

#Decimal to binary
def dec2bin(number):
    val = number
    num_bin = ''
    while(val > 1):
        num_bin+=str(val%2)
        val//=2
    return(str_flip(num_bin[0:len(num_bin)]+'1'))
    #return(num_bin)

# Function to flip a string
def str_flip(a):
    flip_str = ''
    for i in range(len(a)):
        flip_str=flip_str+a[len(a)-i-1]
    return(flip_str)

print(dec2bin(int(input())))