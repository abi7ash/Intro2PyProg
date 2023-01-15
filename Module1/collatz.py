# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:02:53 2023

@author: abilash
"""

#Write a function named collatz() that has one parameter 
#named number. 

#If number is even, then collatz() should
#print number // 2 and return this value. 

#If number is odd, then collatz() should print 
#and return 3 * number + 1.

def collatz(number):
    if((number % 2) == 0):
        print(number//2)
        return(number//2)
    else:
        print((3*number)+1)
        return((3*number)+1)

#write a program that lets the user type in an integer and 
#that keeps calling collatz() on that number until the function
#returns the value 1. 

print("Starting Collatz series...!!!")
while(True):
    print('Enter the number:')
    if(collatz(int(input())) == 1):
        break
print('Collatz ends here...!!')
    