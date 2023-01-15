# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 08:42:28 2022

@author: abilash
"""
# =============================================================================
# ##Basic Import usage
# import random
# for i in range(5):
#     print(random.randint(1, 10))
# =============================================================================
    

# =============================================================================
# ##Alternate Import usage with 'from' keyword
# from random import randint
# for i in range(5):
#     print(randint(1, 10))
# =============================================================================
    
##Import sys and usage of sys.exit 
import sys 
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

