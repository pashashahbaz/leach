# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:07:02 2021

@author: 91750
"""

import random
def create(Area,Model,X,Y):
    n=Model['n']
    x=Area['x']
    y=Area['y']
   
    for i in range(n):
        X[i]=random.random()*x
        Y[i]=random.random()*y
    
    return X,Y