import matplotlib.pyplot as plt
import numpy as np

N_nn, r_nn, V_nn, F_nn = np.loadtxt("neutron-neutron.txt", skiprows = 5, unpack = True)
N_np, r_np, V_np, F_np = np.loadtxt("neutron-proton.txt", skiprows = 5, unpack = True)
N_pp, r_pp, V_pp, F_pp = np.loadtxt("proton-proton.txt", skiprows = 5, unpack = True)

plt.figure(1)
plt.plot(r_nn, V_nn, color = 'blue', label = 'neutron - neutron')
plt.plot(r_pp, V_pp, 'o', color = 'red', label = 'proton - proton')
plt.plot(r_np, V_np, 'o', color = 'green', label = 'neutron - proton')
plt.xlabel(r'Distance $r$', fontsize = 20)
plt.ylabel(r'Potential $V$', fontsize = 20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.legend(numpoints = 1, loc = 'upper right', fontsize = 20)
plt.ylim([0.0,96e3])
plt.xlim([0.0,0.04])

plt.figure(2)
plt.plot(r_nn, F_nn, color = 'blue', label = 'neutron - neutron')
plt.plot(r_pp, F_pp, 'o', color = 'red', label = 'proton - proton')
plt.plot(r_np, F_np, 'o', color = 'green', label = 'neutron - proton')
plt.xlabel(r'Distance $r$', fontsize = 20)
plt.ylabel(r'Force $F$', fontsize = 20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.legend(numpoints = 1, loc = 'upper right', fontsize = 20)
plt.ylim([0.0,1e7])
plt.xlim([0.0,0.04])

plt.show()
