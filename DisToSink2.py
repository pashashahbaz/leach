# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:07:52 2021

@author: 91750
"""
import math
def send(Sensors,Model):
    n=Model['n']
    
    for i in range(n):
        d1=pow(Sensors['xd'][i]-Sensors['xd'][n],2)
        d2=pow(Sensors['yd'][i]-Sensors['yd'][n],2)
        dis=d1+d2
        dis=math.sqrt(dis)
        Sensors['distosink'][i]=dis

    return Sensors