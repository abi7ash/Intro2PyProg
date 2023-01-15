# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 07:08:10 2022

@author: abilash
"""

##List operations

#%% Creating a list
spam = ['cat', 'bat', 'rat', 'elephant'] 

#%% Accessing elements
spam[0]
# 'cat' 
spam[2]
# 'rat'
spam[3] 
# 'elephant'
spam[1]
# 'bat'

#%% Alternate reference to a list
['cat', 'bat', 'rat', 'elephant'][3]
# 'elephant' 

#%% using lists in statements
'Hello ' + spam[0]
#‘Hello cat'

#%% example 2
'The ' + spam[1] + ' ate the ' + spam[0] + '.'
#'The bat ate the cat.'


#%%a.	Negative Indicies
spam[-1]

spam [-3]

#%%b.	Slices and sublists
spam[1:4]

#%%c.	len() function
len(spam)

#%%d.	Modifying lists
spam[3] = '72'

#%%e.	List concatenation
gem = spam + spam

#%%f.	List replication
jeep = spam * 3

#%%del() function
wq = [1,2,3,5]
asw = spam + wq
del(asw[1])

#%%
del(asw[1:4])

#%%in and not in operators



#%%Multiple assignment

p,q,r = asw