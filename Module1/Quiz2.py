# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:41:33 2023

@author: abilash
"""

#%% Q2
listOne = [20, 40, 60, 80] 
listTwo = [20, 40, 60, 80] 
print(listOne == listTwo) 
print(listOne is listTwo)

#%% Q3

listOne = [20, 40, 60, 80] 
listTwo = [20, 40, 60, 80]
listThree = listOne 
print(listOne == listTwo) 
print(listOne is listTwo)
print(listThree == listOne) 
print(listThree is listOne)

#%% Q4

salary = 8000 

def printSalary():
     salary = 12000
     
printSalary()
print("Salary:", salary)
#%% Q5

salary = 8000 

def printSalary(salary):
     salary = 12000
     
printSalary(salary)
print("Salary:", salary)

#%% Q6

salary = 8000 

def printSalary(salary):
     salary = 12000
     return(salary)
     
salary = printSalary(salary)
print("Salary:", salary)

#%% Q7

str = "pynative" 
print (str[1:3])

#%% Q8

str = "pynative" 
print (str[:3])

#%% Q9

for i in range(1, 5):
    print(i)
else:
    print("else block executed" )

#%% Q10

for x in range(0.5, 5.5, 0.5):
  print(x)    

#%% Q11

var= "James Bond"
print(var[2::-1])

#%% Q12

sampleSet = ["Cake", "Pastry", "Bread"]
sampleSet.insert(1,"Pizza")
print(sampleSet)

#%% Q13

sampleSet = ["Cake", "Pastry", "Bread"]
sampleSet.insert(8,"Pizza")
print(sampleSet)

#%% Q14

def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

#%% Q15

def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, )

#%% Q16

'''Please select the correct expression to 
reassign a global variable “x” to 20 
inside a function fun1()'''


x = 50
def fun1():
    # your code to assign global x = 20
    global x 
    x = 20
    
fun1()
print(x) # it should print 20

#%%
'''
#Option A
global var x
x = 20

#Option B
global x = 20

#Option C
global.x = 20

#Option D
global x
x = 20
'''
#%% Q17

def func1():
    x = 50
    return x
func1()
print(x)

#%% Q18
aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))

#%% Q19
aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[1][1:]))

#%% Q20

y = 10
x = y += 2
print(x)

#%% Q21

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

#%% Q22

print(2 * 3 ** 3 * 4)

#%% Q23

print(-18 // 4)

#%% Q24

x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)
