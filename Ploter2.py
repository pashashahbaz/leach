# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:32:56 2021

@author: 91750
"""
import matplotlib.pyplot as plt
def plott(Sensors,Model):
    n=Model['n']
    d=0
    for i in range(n):
        if Sensors['E'][i]>0:
            if Sensors['types'][i]=='N':
                plt.plot(Sensors['xd'][i],Sensors['yd'][i],marker='o')
            else:
                plt.plot(Sensors['xd'][i],Sensors['yd'][i],'kx',markersize=10)
        else:
            d=d+1
            plt.plot(Sensors['xd'][i],Sensors['yd'][i],'red .')
    plt.plot(Sensors['xd'][n],Sensors['yd'][n],marker='*',markersize=15)
    plt.show()
    return d