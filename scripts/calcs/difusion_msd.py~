import numpy as np
import math as m
import matplotlib.pyplot as plt
#-------------------------------------------------------------------
#difusion_msd.py
#-------------------------------------------------------------------
#EL siguiente algoritmo calcula el MSD, (Medium square displacement)
#para cada time-step. MSD(t) y ademas Diffusion(t)

#Author by Tavella Franco y Longo Lucas
#-------------------------------------------------------------------

#1) Elegir un valor para el tiempo de retraso t.

#2) Loop sobre los origenes de tiempo tk {k=1,...,M}.

#3) Para cada origen de tiempo hacemos un loop sobre los N atomos
#i={1,...,N}, para almacenar las posiciones ri(tk)=(xi(tk),yi(tk),zi(tk)).

#4) Desde tk moverse en los datos al tiempo tk+t.

#5) Loop sobre i=1...N, los N atomos para leer ri(tk+t) y acumular en la suma
#msd(t)+=[ri(tk+t)-ri(tk)]^2.

#6) Volver al inicio de los datos y al paso (1) hasta barrer todos los t.

#----------------------------------------------------------------------------
#Preeliminares:
#----------------------------------------------------------------------------

f=open("output_difusion_sorted_true.lammpstrj")
lines=f.readlines()


#Numero de particulas
Numpart=int(lines[3])

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
timestep=[]
lookup = 'ITEM: ATOMS id type x y z vx vy vz'
k=0

with open("output_difusion_sorted_true.lammpstrj") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart.append(num)
            dataend.append(num+Numpart-1)
            #Vector de time-steps:
            timestep.append(k)
            k=k+1

print 'Vector de time-steps:'
print timestep


#-----------------------------------------------------------------------------
#MSD
#-----------------------------------------------------------------------------

msd=np.zeros(len(timestep))

g=open('output_difusion_msd.txt','w')
g.write('time-step   Msd  Diffusion \n')


for tdelay in range(1,len(timestep)-150): #los primeros 50 steps 150=200-50
    suma=0
    for torigin in range(0,len(timestep)-tdelay):
        for n in range(0,Numpart):
            if int(lines[datastart[torigin]+n].split(' ')[1])==1:  #id 1:Neutrones 2:Protones
                xorigin= float(lines[datastart[torigin]+n].split(' ')[2])
                xdelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[2])
                yorigin= float(lines[datastart[torigin]+n].split(' ')[3])
                ydelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[3])
                zorigin= float(lines[datastart[torigin]+n].split(' ')[4])
                zdelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[4])
                dx=xdelay-xorigin
                dy=ydelay-yorigin
                dz=zdelay-zorigin
                dr=(dx**2+dy**2+dz**2)
                suma+=dr
    msd[tdelay]=suma/(Numpart*(len(timestep)-tdelay)) #promedio en part y tiempo
    g.write(str(tdelay)+' '+str(msd[tdelay])+' '+str(float(msd[tdelay])/float((6*tdelay)))+'\n')
    print 'Done with tdelay '+str(tdelay)+'\n'

g.close()
