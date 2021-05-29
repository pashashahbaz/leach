# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:27:28 2021

@author: 91750
"""

import random
import math

def select(TotalCH,Sensors,Model,r):
    countCH=0
    n=Model['n']
    for i in range(n):
        if Sensors['E'][i]>0:
            temp_rand=random.uniform(0,1)
            if Sensors['G'][i]<=0:
                if temp_rand<= (Model['p']/(1-Model['p']*(math.fmod(r,round(1/Model['p']))))):
                    countCH=countCH+1
                    Sensors['types'][i]='C'
                    Sensors['G'][i]=round(1/Model['p'])-1
                    
                    TotalCH.append(i+1)
    
    return TotalCH,Sensors