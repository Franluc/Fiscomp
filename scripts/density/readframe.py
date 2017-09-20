################################################################
# Script for calculating the density distribution
# from a lammps trajectory's frame in a multiparticle system
#
#
# Authors: Lucas Longo and Franco Tavella
#
################################################################
import numpy as np
import matplotlib.pyplot as plt


N = 6000 # Total atoms
L = 42.2 # Box size
m = 100 # Sub boxes in each direction
b = L/m # Sub box length

data_file = "oneframe.txt"

# Header
header_lines = 9
with open(data_file) as myfile:
    header = [next(myfile) for x in xrange(header_lines)]
# Values
[id_vals, type_vals, x, y, z, vx, vy, vz] = np.genfromtxt(data_file, skip_header = 9, unpack = True)

tstep = int(header[1]) # Timestep

x_slab = np.zeros(m)
y_slab = np.zeros(m)
z_slab = np.zeros(m)

count_grid = np.zeros((m,m,m))

# Number of particles in each sub box and slabs
for idx in range(N):
    if type_vals[idx]==2: # One type of particle

        # Indexes
        sub_x = int(x[idx] / b)
        sub_y = int(y[idx] / b)
        sub_z = int(z[idx] / b)

        # Sub box
        count_grid[sub_x][sub_y][sub_z] += 1.0

        # Slabs
        x_slab[sub_x] += 1.0
        y_slab[sub_y] += 1.0
        z_slab[sub_z] += 1.0

# Densities
dens = count_grid / np.power(b,3)

# Grid points
grid = [i*b for i in range(m)]

plt.plot(grid,x_slab,'-o', label = 'x slab')
plt.plot(grid,y_slab,'-o', label = 'y slab')
plt.plot(grid,z_slab,'-o', label = 'z slab')
plt.legend(numpoints = 1)
plt.show()


'''
# 3D plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(N):
    if type_vals[i] == 1:
        ax.scatter(x[i], y[i], z[i], color = 'blue')
    elif type_vals[i] == 2:
        ax.scatter(x[i], y[i], z[i], color = 'red')
plt.show()
'''
