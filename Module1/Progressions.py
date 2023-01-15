# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:16:40 2023

@author: abilash
"""

#%% Arithmetic Progression

def ap_gen():
    print('Enter data for series..!!!')
    print('Enter the first term:')
    a = int(input())
    print('Enter the number of terms:')
    n = int(input())
    print('Enter the difference:')
    d = int(input())
    
    #series
    ap_ser = []
    for i in range(1,n+1):
        # print(a+((i-1)*d))
        ap_ser.append(a+((i-1)*d))
    return(ap_ser)

def gp_gen():
    print('Enter data for series..!!!')
    print('Enter the first term:')
    a = int(input())
    print('Enter the number of terms:')
    n = int(input())
    print('Enter the ratio between consecutive terms:')
    r = int(input())
    
    #series
    gp_ser = []
    for i in range(1,n+1):
        # print(a+((i-1)*d))
        gp_ser.append(a*(r**(i-1)))
    return(gp_ser)


while(True):
    print('Welcome to the Progression Engine..!!')
    print('Enter option to generate progression')
    print('0.Exit\n1. Arithmetic Progression\n2. Geomteric Progression\n')
    opt_val = int(input())
    if(opt_val == 0):
        break
    elif(opt_val == 1):
        my_pre = ap_gen()
    else:
        my_pre = gp_gen()
        
    print('What do you want with this progression?')
    print('Select options:')
    print('\n1. nth Term\n2.Sum of n-terms')
    opt_val = int(input())
    if(opt_val == 1):
        print('For the series ',my_pre)
        print('term ',len(my_pre),' in given series is ',my_pre[len(my_pre)-1],'\n\n\n')
    else:
        sum=0
        for i in range(len(my_pre)):
            sum+=my_pre[i]
        print('For the series ',my_pre)
        print('The sum of terms is ',sum,'\n\n\n')
    
    

