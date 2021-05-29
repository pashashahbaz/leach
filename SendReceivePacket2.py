# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:51:52 2021

@author: 91750
"""
import math
def packet(Sensors,Model,Sender,PacketType,Receiver,srp,rrp,sdp,rdp):
    sap=0
    rap=0
    if PacketType=='Hello':
        PacketSize=Model['HpacketLen']
    else:
        PacketSize=Model['DpacketLen']
    d1=Sensors['xd'][0]-Sensors['yd'][Receiver[0]-1]
    for i in range(len(Sender)):
        for j in range(len(Receiver)):
            d1=Sensors['xd'][Sender[i]-1]-Sensors['xd'][Receiver[j]-1]
            d2=Sensors['yd'][Sender[i]-1]-Sensors['yd'][Receiver[j]-1]
            d1=d1*d1
            d2=d2*d2
            distance=math.sqrt(d1+d2)
            if distance>Model['d']:
                Sensors['E'][Sender[i]-1]=Sensors['E'][Sender[i]-1]-(Model['Etx']*PacketSize +Model['Emp']*PacketSize*pow(distance,4))
                if Sensors['E'][Sender[i]-1]>0:
                    sap=sap+1
            else:
                Sensors['E'][Sender[i]-1]=Sensors['E'][Sender[i]-1]-(Model['Etx']*PacketSize +Model['Efs']*PacketSize*pow(distance,2))
                if Sensors['E'][Sender[i]-1]>0:
                    sap=sap+1
        
    for i in range(len(Receiver)):
        Sensors['E'][Receiver[i]-1]=Sensors['E'][Receiver[i]-1]-((Model['Erx']+Model['Eda'])*PacketSize)
    for i in range(len(Sender)):
        for j in range(len(Receiver)):
            if Sensors['E'][Sender[i]-1]>0 and Sensors['E'][Receiver[j]-1]>0:
                rap=rap+1
    if PacketType=='Hello':
        srp=srp+sap
        rrp=rrp+rap
    else:
        sdp=sdp+sap
        rdp=rdp+sap
    
    return Sensors,srp,rrp,sdp,rdp