# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:33:46 2023

@author: abilash
"""

#%% Dictionary

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

myCat['size']

'My cat has ' + myCat['color'] + ' fur.'


#%% Usage of keys(),values() and items() methods

print('myCat.keys() prints:',myCat.keys())
print('\n\nmyCat.items() prints:',myCat.items())
print('\n\nmyCat.values() prints:',myCat.values())
#%% Datatype 

print('Type of type(myCat.keys()) is ',type(myCat.keys()))
print('\nType of type(myCat.values()) is ',type(myCat.values()))
print('\nType of type(myCat.items()) is ',type(myCat.items()))
#%% Usage for dict access using keys() method
for v in myCat.keys():
    print(v)

#%%

for v in myCat.items():
    print(v)
    
#%%

for v in myCat.values():
    print(v)

#%% usage of in and not in operators

'fat' in myCat
'fat' in myCat.items()
'color' in myCat.keys()
'fat' in myCat.values()




