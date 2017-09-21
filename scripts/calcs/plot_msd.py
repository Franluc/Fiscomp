import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#----------------------------------------------------------------------------
#plot_msd.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma el archivo de msd y extrae un coeficiente de
#difusion en el regimen lineal

#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------
def lineal(x,a,b):
    y = a * x + b
    return y

data = np.genfromtxt('output_difusion_msd.txt', names = True)
#print(data.dtype.names)
#Linear fit
xdata = data['timestep']
ydata = data['Msd']
popt, pcov = curve_fit(lineal, xdata, ydata)
perr = np.sqrt(np.diag(pcov))
D = popt[0]/6.0
Derr = perr[0]/6.0
print('Diffusion Coef: ' + str(D) + ' err: ' + str(Derr))
xfit = np.linspace(0,50,1000)
yfit = lineal(xfit, popt[0], popt[1])
plt.plot(xfit, yfit, color = 'red', linewidth = 3.0)
plt.plot(xdata , ydata, 'o', color = 'blue', markersize = 6.0)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlabel('Time Step', fontsize = 30)
plt.ylabel('MSD', fontsize = 30)
plt.show()
