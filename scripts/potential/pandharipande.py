import numpy as np
import matplotlib.pyplot as plt
V_r = 2.0
V_a = 1.0
mu_r = 1.0
mu_a = 0.5
r_c = 10.0
def V_np(x):
	y_r = V_r*(np.exp(-mu_r*x)/x - np.exp(-mu_r*r_c)/r_c) 
	y_a = V_a*(np.exp(-mu_a*x)/x - np.exp(-mu_a*r_c)/r_c)
	y = y_r - y_a
	return y
x = np.linspace(0,20,1000)
y = V_np(x)
plt.plot(x,y,'o')
plt.show()

