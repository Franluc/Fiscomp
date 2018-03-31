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

data = np.genfromtxt('difusion_T_4.0_msd_N_true.txt', names = True)
#print(data.dtype.names)
#Linear fit
xdata = data['timestep']
ydata = data['Msd']
errory=data['SigmaMsd']
popt, pcov = curve_fit(lineal, xdata, ydata,sigma=errory)
perr = np.sqrt(np.diag(pcov))
D = popt[0]
Derr = perr[0]
print('Diffusion Coef: ' + str(D) + ' err: ' + str(Derr))
xfit = np.linspace(0,1000,5)
yfit = lineal(xfit, popt[0], popt[1])
plt.plot(xfit, yfit, color = 'red', linewidth = 3.0)
plt.errorbar(xdata , ydata, errory, fmt='bo', color = 'blue', markersize = 6.0,label='pendiente '+str(float("{0:.3f}".format(popt[0])))+'+-'+str(float("{0:.3f}".format(np.sqrt(pcov[0,0])))))
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xlabel('Time Step', fontsize = 10)
plt.ylabel('MSD', fontsize = 10)
plt.title('Temperatura 4.0')
plt.legend()
plt.show()
