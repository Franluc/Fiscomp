import numpy as np
import math as m
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#difusion_simpson.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma el archivo de funcion de autocorrelacion de
#velocidades y realiza una integracion mediante la regla de integracion
#de Simpson.


#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------

#------------------------------------------------------------------------------
#FAV: Autocorrelation velocities function
#-----------------------------------------------------------------------------
data = np.genfromtxt('difusion_fav_N_T_4.0.txt', names = True)

#print(data.dtype.names)
xdata=data['timestep']
data_favx=data['fav_x']
data_favy=data['fav_y']
data_favz=data['fav_z']
favtotal=(data_favx/data_favx[0])+(data_favy/data_favy[0])+(data_favz/data_favz[0])

#El numero de areas de parabolas para integrar es:

##ndata=len(data_fav_total_N)
ndata=len(favtotal)
nareas=np.floor((ndata-1)/2)
print ('Integracion de la funcion VACF mediante la regla Simpson')
print ('Numero de puntos: '+str(ndata))
print ('Numero de areas de Simpson: '+str(nareas))

integral_N=0
areas_N=[]
for i in range (0,len(data)-2,2):
## area_N=((xdata[i+2]-xdata[i])/6)*(data_fav_total_N[i]+4*data_fav_total_N[i+1]+data_fav_total_N[i+2])
 area_N=((xdata[i+2]-xdata[i])/6)*(favtotal[i]+4*favtotal[i+1]+favtotal[i+2])
 areas_N.append(area_N)
 integral_N=integral_N+area_N
 
print ('Integral de VACF neutrones='+str(integral_N))

plt.show()


