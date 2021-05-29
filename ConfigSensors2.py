# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:12:40 2021

@author: 91750
"""

import math
def sensor(Area,Model,X,Y,xd,yd,G,df,types,E,ids,distosink,distoCH,MCH):
    n=Model['n']
    for i in range(n):
        xd.append(X[i])
        yd.append(Y[i])
        G.append(0)
        df.append(0)
        types.append('N')
        E.append(Model['Eo'])
        ids.append(i+1)
        distosink.append(0)
        distoCH.append(0)
        MCH.append(101)
    xd.append(Model['sinkx'])
    yd.append(Model['sinky'])
    G.append(0)
    df.append(0)
    types.append('C')
    E.append(Model['Eo'])
    ids.append(i+1)
    distosink.append(0)
    distoCH.append(0)
    MCH.append(101)
    return xd,yd,G,df,types,E,ids,distosink,distoCH,MCH
    
        
    