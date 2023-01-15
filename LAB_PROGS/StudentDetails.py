# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:21:44 2022

@author: abilash
"""

#Program to print the student details

#%%Reading details from the keyboard
print("Enter the name of the student : ")
name=input()

print("Enter the USN of the student : ")
usn=input()

print("Enter the marks in the first subject : ")
marks1=int(input())

print("Enter the marks in the second subject : ")
marks2=int(input())

print("Enter the marks in the third subject : ")
marks3=int(input())

#%%calculations
total=marks1+marks2+marks3
percentage=total*100/300

#%%Printing the student details
print("The name of the student is : ", name)
print("The USN of the student is : ", usn)
print("Marks in the first subject : ", marks1)
print("Marks in the second subject : ", marks2)
print("Marks in the Third subject : ", marks3)
print("The total marks scored by the student : ", total)
print("The percentage marks is : ","%0.4f" % percentage)