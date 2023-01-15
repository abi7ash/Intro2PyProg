# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:11:45 2023

@author: abilash
"""
import pprint

message = 'I love it when a plan comes together!!'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
# print(count)