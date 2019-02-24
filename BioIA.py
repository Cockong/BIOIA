#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:07:26 2019

@author: remi
"""

import numpy as np

def check(garage,IA,voiture):
    resultat=np.sum(garage.dot(IA))
    print(resultat)
    if  resultat < 0.33 :
        porte = 1
    elif resultat < 0.66 :
        porte = 2
    else :
        porte = 3
    print(porte)
    return(porte==voiture)




garage = [ np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1]) ]
voiture= [ 1 ,2 , 3]

groupe=list()

for i in range(1000) :
    groupe.append( np.random.rand(3,1) )

test=list()
for IA in groupe :
    checking= check(garage[0],IA,voiture[0]) + check(garage[1],IA,voiture[1]) + check(garage[2],IA,voiture[2])
    if checking >2 :
        test.append((IA,True ))
    else :
        test.append((IA,False ))

count=0
gagnants=list()

for output in test:
    if output[1]==True:
        count+=1
        gagnants.append(output[0])
        
"""
solution=np.array([ [0.3] , [0.6] , [0.9] ])
"""