# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:33:46 2023

@author: abilash
"""

#%% Dictionary

myCat = {'name':'Ji-min','age(in yrs)': 4,'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

#%%
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

#%% The get method

myCat.get('name')

#%%

'My Cat '+ myCat.get('name') + ' is of age ' + str(myCat.get('age'))+' years'

#%% Returns None type

str(myCat.get('age'))

#%%

'age' in myCat

#%% Returns 0 with optional arguments in get method

str(myCat.get('age',0))

#%%

'age(in yrs)' in myCat


#%% Working method

str(myCat.get('age(in yrs)',0))

#%% without the get() method

'My cat '+ myCat['name'] +' is ' + myCat['fat'] + '.'

#%% usage of get() method

'My cat '+ myCat.get('name',0) +'  is of age ' + str(myCat.get('age(in yrs)',0))+ '.'

#%%
myCat['color']

#%% Existing key case
print('altering myCat\'s color to blue using setdefault() method')
myCat.setdefault('color','blue')
print(myCat['color'])

#%% Non-existing key
print('myCat\'s eyes are colored '+myCat.get('eyes','0')+'.')

#%% Setdefault() for non-existing key
myCat.setdefault('eyes','green')
print('myCat\'s eyes are colored '+myCat.get('eyes','0')+'.') 
#%%