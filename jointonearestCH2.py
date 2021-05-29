# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:51:58 2021

@author: 91750
"""
import math
import numpy as np
def Join(Sensors,Model,TotalCH):
    n=Model['n']
    m=len(TotalCH)
    if m>1:
        D=[]
        for i in range(m):
            B=[]
            for j in range(n):
                B.append(0)
            D.append(B)
            
        for i in range(n):
            for j in range(m):
                d1=pow(Sensors['xd'][i]-Sensors['xd'][TotalCH[j]-1],2)
                d2=pow(Sensors['yd'][i]-Sensors['yd'][TotalCH[j]-1],2)
                D[j][i]=math.sqrt(d1+d2)
        arr=np.array(D)
        Dmin=[]
        Din=[]
        Dmin=arr.min(axis=0)
        for i in range(n):
            x=Dmin[i]
            for j in range(m):
                if D[j][i]==x:
                    Din.append(j)
                    break
        for i in range(n):
            if Sensors['E'][i]>0:
                if Dmin[i]<=Model['RR'] and Dmin[i]<Sensors['distosink'][i]:
                    Sensors['MCH'][i]=TotalCH[Din[i]]
                    Sensors['distoCH']['i']=Dmin[i]
                else:
                    Sensors['MCH'][i]=n+1
                    Sensors['distoCH'][i]=Sensors['distosink'][i]
    return Sensors
                    
                
                
        
        
        
                
                