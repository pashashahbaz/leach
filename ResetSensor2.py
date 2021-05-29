# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 10:15:12 2021

@author: 91750
"""

def reset(Sensor,Model):
    n=Model['n']
    for i in range(n):
        Sensor['MCH'][i]=n+1
        Sensor['types'][i]='N'
        Sensor['distoCH'][i]=float('inf')

    return Sensor