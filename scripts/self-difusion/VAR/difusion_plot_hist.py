import numpy as np
import math as m
import matplotlib.pyplot as plt
from pylab import *
from numpy import loadtxt
from scipy.optimize import leastsq
#-------------------------------------------------------------------
#difusion_plot.py
#-------------------------------------------------------------------
#EL siguiente algoritmo grafica todos los histogramas
#Author by Tavella Franco y Longo Lucas
#-------------------------------------------------------------------



#----------------------------------------------------------------------------
#Preeliminares:
#----------------------------------------------------------------------------
plt.figure(1)
for tdelay in range(1,1000,100):
 f=open('hist_T_4.0_tdelay_'+str(tdelay)+'.txt')
 lines=f.readlines()
 Temp=lines[2]

 #Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
 datastart=0
 dataend=0
 lookup = 'centro  cuenta'
 lookup2= 'Gaussian Fit:'
 k=0
 centros=[]
 histo=[]
 with open('hist_T_4.0_tdelay_'+str(tdelay)+'.txt') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart=num
        if lookup2 in line:
            dataend=num-1
    for line in range(datastart,dataend):
     centros.append(float((lines[line].split()[0])))
     histo.append(float((lines[line].split()[1])))

   
    plt.bar(centros,histo,width=centros[1]-centros[0],edgecolor='k',label='tdelay '+str(tdelay))

plt.xlabel('DeltaX,Y,Z')
plt.legend()
plt.title('Temperatura '+str(Temp))
plt.show()




   
