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
data = np.genfromtxt('output_difusion_fav_Z.txt', names = True)
data2= np.genfromtxt('output_difusion_fav_N.txt', names = True)
#print(data.dtype.names)
xdata=data['timestep']
data_favx=data['fav_x']
data_favy=data['fav_y']
data_favz=data['fav_z']
data_fav_total_Z=data['fav_total']
data_fav_total_N=data2['fav_total']

#El numero de areas de parabolas para integrar es:

ndata=len(data_fav_total_Z)
nareas=np.floor((ndata-1)/2)
print 'Integracion de la funcion VACF mediante la regla Simpson'
print 'Numero de puntos: '+str(ndata)
print 'Numero de areas de Simpson: '+str(nareas)

integral_Z=0
areas_Z=[]
integral_N=0
areas_N=[]
for i in range (0,len(data)-2,2):
 area_Z=((xdata[i+2]-xdata[i])/6)*(data_fav_total_Z[i]+4*data_fav_total_Z[i+1]+data_fav_total_Z[i+2])
 area_N=((xdata[i+2]-xdata[i])/6)*(data_fav_total_N[i]+4*data_fav_total_N[i+1]+data_fav_total_N[i+2])
 areas_Z.append(area_Z)
 areas_N.append(area_N)
 integral_Z=integral_Z+area_Z
 integral_N=integral_N+area_N
 
print 'Integral de VACF protones='+str(integral_Z)
print 'Integral de VACF neutrones='+str(integral_N)



'''
plt.figure(5)
plt.plot(xdata,data_favx,'-o',color='g',markersize=6.0,label='vacfx')
plt.plot(xdata,data_favy,'-o',color='r',markersize=6.0,label='vacfy')
plt.plot(xdata,data_favz,'-o',color='c',markersize=6.0,label='vacfz')
plt.plot(xdata,data_fav_total,'-o',color='m',markersize=6.0,label='vacf_total')
plt.title('Velocity Autocorrelation Function')
plt.xlabel('time-step')
plt.ylabel('VACF')
plt.legend(loc='upper right')
'''
plt.show()


