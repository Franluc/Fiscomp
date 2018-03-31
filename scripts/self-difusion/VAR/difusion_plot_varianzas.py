import numpy as np
import math as m
import matplotlib.pyplot as plt
from pylab import *
from numpy import loadtxt
from scipy.optimize import leastsq
from scipy.optimize import curve_fit
#-------------------------------------------------------------------
#difusion_plot.py
#-------------------------------------------------------------------
#EL siguiente algoritmo grafica la varianza de los histogramas o sea el
#sigma**2 vs el tdelay y realiza un fit para obtener la pendiente del ajuste
#la cual esta relacionada con el coef de Difusion
#Author by Tavella Franco y Longo Lucas
#-------------------------------------------------------------------
#Preeliminares:
#----------------------------------------------------------------------------
def func(x, a, b):
    return a*x+b

plt.figure(1)
t=[]
var=[]
errvar=[]

for tdelay in range(1,1000,100):
 f=open('hist_T_4.0_tdelay_'+str(tdelay)+'.txt')
 lines=f.readlines()
 Temp=lines[2]

 #Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
 datastart=0
 dataend=0
 lookup = 'tdelay'
 lookup2= 'Gaussian Fit:'
 k=0

 with open('hist_T_4.0_tdelay_'+str(tdelay)+'.txt') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart=num
        if lookup2 in line:
            dataend=num+1
    t.append(float((lines[datastart].split()[0])))
    var.append(float((lines[dataend].split()[3])))
    errvar.append(float((lines[dataend].split()[6])))
    
#fit
xdata = t
ydata = var

popt, pcov= curve_fit(func,xdata,ydata,sigma=errvar)

print ('Parametros')
print('Pendiente '+str(popt[0]))
print('Ordenada '+str(popt[1]))
print ('Covarianza')
print(pcov)

fit=[]
for j in range(0,len(t)):
 fit.append(func(t[j],*popt))

plt.errorbar(t, var,errvar, fmt='bo')
plt.plot(t,fit,'r-',label='pendiente '+str(float("{0:.3f}".format(popt[0])))+'+-'+str(float("{0:.3f}".format(np.sqrt(pcov[0,0])))))
plt.xlabel('tdelay')
plt.ylabel('Varianza')
plt.title('Temperatura'+str(Temp))
plt.legend()
plt.show()
   
