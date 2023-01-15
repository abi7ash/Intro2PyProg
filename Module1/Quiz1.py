# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:56:24 2023

@author: abilash
"""

# Quiz 1

#%% Q4

pin = 24
a = 'pin'
print(a)

#%% Q8

bacon = 16
bacon + 2
print(bacon)

#%% Q9

a = 'Hi'
print(a*len(a))


#%% Q10

a = 'Hi'
print(a**len(a))

#%% Q11

a = 12
b = 16
12 = a +b

#%% Q12

a = 2
c = a*str(a)
print(c*int(c))

#%% Q13

Gems = 1000
Gems == 'gems'

#%%

print('I have eaten ' , 99, ' burritos.')

#%%

jum=100
if(jum-jum):
    print('Skip Trace')
print('Done..!!!')

#%%
snake = 'Anaconda'
while True:
    print(snake)
print('Thank you!')

#%% Program A
for i in range(6):
    print(i)

#%% Program B
for i in range(1,6,2):
    print(i)

#%% Program C
for i in range(1,10,3):
    print(i)
    
#%%  Q26
import random

def checkstr(cstr):
    
    if(type(cstr) == str):
        P = cstr
        return(P+'is a string')
    else:
        Q = str(cstr)
        return(Q+' is not a string')

ip_str = 12
m = checkstr(ip_str)
print(m)