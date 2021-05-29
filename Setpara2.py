# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:04:31 2021

@author: 91750
"""

import math
def setp(Area,Model,n):
    Area={'x':100,'y':100}
    sinkx=0.5*Area['x']
    sinky=sinkx
    p=0.1
    Eo=0.5
    Etx=50*0.000000001
    Erx=50*0.000000001
    Efs=10*0.000000000001
    Emp=0.0013*0.000000000001
    Eda=5*0.000000001
    d=math.sqrt(Efs/Emp)
    rmax=5000
    DpacketLen=4000;

    
    HpacketLen=100;
    
    
    NumPacket=10;
    RR=0.5*Area['x']*math.sqrt(2)
    Model['n']=n
    Model['sinkx']=sinkx
    Model['sinky']=sinky
    Model['p']=p
    Model['Eo']=Eo
    Model['Etx']=Etx
    Model['Erx']=Erx
    Model['Efs']=Efs
    Model['Emp']=Emp
    Model['Eda']=Eda
    Model['d']=d
    Model['rmax']=rmax
    Model['RR']=RR
    Model['DpacketLen']=DpacketLen
    Model['HpacketLen']=HpacketLen
    Model['NumPacket']=NumPacket
    
    
    return Area,Model
    
    

    