import numpy as np
import math as m
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#difusion_plot.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma los archivos de densidades out_densidades_Z
#y out_densidades_N y realiza dos graficos uno para protones y otro para
#neutrones mostrando la densidades a lo largo de pasos temporales elegidos
# por el usuario en el vector timestep=[,,].
#Ademas grafica el MSD, FAV, y D


#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------

#------------------------------------------------------------------------------
#FAV: Autocorrelation velocities function
#-----------------------------------------------------------------------------
data = np.genfromtxt('difusion_fav_N_T_4.0.txt', names = True)

xdata=data['timestep']
data_favx_N=data['fav_x']
data_favy_N=data['fav_y']
data_favz_N=data['fav_z']
data_fav_total_N=data['fav_total']
##favtotal=data_favx_N/data_favx_N[0]+data_favy_N/data_favy_N[0]+data_favz_N/data_favz_N[0]

plt.figure(5)

plt.plot(xdata,data_favx_N,'-o',color='g',markersize=6.0,label='vacfx')
plt.plot(xdata,data_favy_N,'-o',color='r',markersize=6.0,label='vacfy')
plt.plot(xdata,data_favz_N,'-o',color='c',markersize=6.0,label='vacfz')
plt.plot(xdata,data_fav_total_N,'-o',color='m',markersize=6.0,label='vacf_total')
##plt.plot(xdata,favtotal,'-o',color='m',markersize=6.0,label='vacf_total')

plt.title('Velocity Autocorrelation Function '+'\n'+'Temperatura 4.0'+'\n')
plt.xlabel('time-step')
plt.ylabel('VACF')
plt.legend(loc='upper right')


plt.show()


