# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:37:07 2021

@author: 91750
"""

import math

def find(Sensors,Model,sender,receiver,senderRR):
    n=Model['n']
    D=[0]*n
    
    for i in range(n):
        d1=Sensors['xd'][i]-Sensors['xd'][sender[0]-1]
        d2=Sensors['yd'][i]-Sensors['yd'][sender[0]-1]
        d1=d1*d1
        d2=d2*d2
        dis=math.sqrt(d1+d2)
        D[i]=dis
        
        
    for i in range(n):
        if D[i]<=senderRR and (sender[0] != Sensors['ids'][i]):
            d=Sensors['ids'][i]
            receiver.append(d)
    
    return receiver