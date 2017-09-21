import numpy as np
import math as m
import matplotlib.pyplot as plt


#----------------------------------------------------------------------------
#difusion_sortdata.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma cada timestep en el archivo output_difusion
# y ordena las particulas por su id, desde 1 hasta Numpart. Imprime el archivo
#output_difusion_sorted.lammpstrj

#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------

#Densidad de protones
f=open("output_difusion.lammpstrj")
lines=f.readlines()

#Numero de particulas
Numpart=int(lines[3])

#Dimension de celda
xlo=float(lines[5].split(' ')[0])#xlo
xhi=float(lines[5].split(' ')[1])#xhi
ylo=float(lines[6].split(' ')[0])#ylo
yhi=float(lines[6].split(' ')[1])#yhi
zlo=float(lines[7].split(' ')[0])#zlo
zhi=float(lines[7].split(' ')[1])#zhi

#Recorro y encuentro los time-steps y me los guardo
timestep=[]
lookup = 'ITEM: TIMESTEP'
with open("output_difusion.lammpstrj") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            timestep.append(int(lines[num]))

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
lookup = 'ITEM: ATOMS id type x y z vx vy vz '

with open("output_difusion.lammpstrj") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart.append(num)
            dataend.append(num+Numpart-1)

g=open('output_difusion_sorted.lammpstrj','w')

for t in range(0,len(timestep)):
 g.write('ITEM: TIMESTEP\n')
 g.write(str(timestep[t])+'\n')
 g.write('ITEM: NUMBER OF ATOMS\n')
 g.write(str(Numpart)+'\n')
 g.write('ITEM: BOX BOUNDS pp pp pp\n')
 g.write(str(xlo)+' '+str(xhi)+'\n')
 g.write(str(ylo)+' '+str(yhi)+'\n')
 g.write(str(zlo)+' '+str(zhi)+'\n')
 g.write('ITEM: ATOMS id type x y z vx vy vz \n')
 orden=np.zeros(Numpart)
 for i in range(datastart[t],dataend[t]+1):
     orden[int(lines[i].split(' ')[0])-1]=i
 for o in orden:
  g.write(str(lines[int(o)].split(' ')[0])+' '+str(lines[int(o)].split(' ')[1])+' '+str(lines[int(o)].split(' ')[2])+' '+str(lines[int(o)].split(' ')[3])+' '+str(lines[int(o)].split(' ')[4])+' '+str(lines[int(o)].split(' ')[5])+' '+str(lines[int(o)].split(' ')[6])+' '+str(lines[int(o)].split(' ')[7])+'\n')

g.close()
