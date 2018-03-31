import numpy as np
import math as m
import matplotlib.pyplot as plt
from pylab import *
from numpy import loadtxt
from scipy.optimize import leastsq
from scipy.optimize import curve_fit
#-------------------------------------------------------------------
#difusion_hist.py
#-------------------------------------------------------------------
#EL siguiente algoritmo calcula un histograma con los DeltaX, DeltaY
#DeltaZ para cada tdelay a la temperaturas T_*.
#Author by Tavella Franco y Longo Lucas
#-------------------------------------------------------------------
#Preeliminares:
#----------------------------------------------------------------------------
def func(x, a, b,c):
    return a*exp(-0.5*((x-b)/c)**2)

f=open("difusion_T_4.0_sorted_true.lammpstrj")
lines=f.readlines()


#Numero de particulas
Numpart=int(lines[3])

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
timestep=[]
lookup = 'ITEM: ATOMS id type x y z vx vy vz'
k=0

with open('difusion_T_4.0_sorted_true.lammpstrj') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart.append(num)
            dataend.append(num+Numpart-1)
            #Vector de time-steps:
            timestep.append(k)
            k=k+1
#-----------------------------------------------------------------------------
#Preparacion de los datos, calculo los deltax y los guardo.
#----------------------------------------------------------------------------

for tdelay in range(1,1000,100):
    data=[]
    for torigin in range(0,len(timestep)-tdelay):
        for n in range(0,Numpart):
            if int(lines[datastart[torigin]+n].split(' ')[1])==1:  #id 1:Neutrones 2:Protones
                xorigin= float(lines[datastart[torigin]+n].split(' ')[2])
                xdelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[2])
                yorigin= float(lines[datastart[torigin]+n].split(' ')[3])
                ydelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[3])
                zorigin= float(lines[datastart[torigin]+n].split(' ')[4])
                zdelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[4])
                dx=xdelay-xorigin
                data.append(dx)
                dy=ydelay-yorigin
                data.append(dy)
                dz=zdelay-zorigin
                data.append(dz)
##    print(len(data))

    hist, bin_edges = np.histogram(data, bins=100, density=True)
    centros=[]
    for b in range(0,len(bin_edges) - 1):
     centros.append((bin_edges[b+1]+bin_edges[b])/2)
                  
    g=open('hist_T_4.0_tdelay_'+str(tdelay)+'.txt','w')
    g.write('Histograma'+'\n')
    g.write('T'+'\n')
    g.write(str(4.0)+'\n')
    g.write('tdelay'+'\n')
    g.write(str(tdelay)+'\n')
    g.write('centro  cuenta'+'\n')

    #fit
  
    xdata    = centros
    ydata    = hist
 
    popt, pcov= curve_fit(func,xdata,ydata)

    fit=[]
    for j in range(0,len(centros)):
     fit.append(func(centros[j],*popt))

    for h in range(0,len(centros)):
     g.write(str(xdata[h])+' '+str(ydata[h])+'\n')

    g.write('Gaussian Fit:'+'\n')
    g.write('Amp'+' '+'mu'+' '+'sigma'+' '+'var'+' '+'dmu'+' '+'dsigma'+' '+'dvar'+'\n')
    g.write(str(popt[0])+' '+str(popt[1])+' '+str(abs(popt[2]))+' '+str(np.power(popt[2],2))+' '+str(np.sqrt(pcov[1,1]))+' '+str(np.sqrt(pcov[2,2]))+' '+str(2*popt[2]*np.sqrt(pcov[2,2]))+'\n')

    g.close()

    #grafico
    plt.bar(centros,hist,width=bin_edges[1]-bin_edges[0],align='center',edgecolor='k')
    plot(xdata, fit,'r')
    plt.show()

    print ('Done with hist_tdelay'+str(tdelay)+'\n')



