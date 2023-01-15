# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:41:04 2022

@author: abilash
"""

"""
Read N numbers from the console and create a list.
Develop a program to print mean, variance 
and standard deviation with suitable messages. 
"""

print("This program provides mean,variance and standard deviation for a list of numbers.")
print("Please enter the size of the list:")
lsiz = int(input())

#%%Create emply list of specified size
lst=[0]
lst = lst*lsiz

#%% Get list input 
print("Enter the terms:")
for i in range(0,lsiz):
    print("Enter term",i+1,":")
    lst[i] = int(input())

#%% Calculate mean
mean = 0
for i in range(lsiz):
    mean+=lst[i]
mean/=lsiz

#%% Calculate variance 
var = 0
for i in range(lsiz):
    var+=(lst[i]-mean)**2
var/=lsiz

#%% Calculate Standard Deviation
std_dev=var**(0.5)

#%%Print Mean, Variance and Standard Deviation
print("For the given list ",lst)
print("Mean = ",mean)
print("Variance =",var)
print("Standard Deviation = ",std_dev)

