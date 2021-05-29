# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:03:34 2021

@author: 91750
"""

def find(Sensors,Model,Receiver,Sender):
    n=Model['n']
    for i in range(n):
        if Sensors['MCH'][i]==Receiver[0] and Sensors['id'][i]==Receiver[0]:
            Sender.append(Sensors['id'][i])
            
    return Sender
