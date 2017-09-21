import numpy as np
import math as m
import matplotlib.pyplot as plt
#-------------------------------------------------------------------
#difusion_fav.py
#-------------------------------------------------------------------
#EL siguiente algoritmo calcula la funcion de autocorrelacion de las
#velocidades fav(t) para cada time-step.

#Author by Tavella Franco y Longo Lucas
#-------------------------------------------------------------------

#1) Elegir un valor para el tiempo de retraso t.

#2) Loop sobre los origenes de tiempo tk {k=1,...,M}.

#3) Para cada origen de tiempo hacemos un loop sobre los N atomos
#i={1,...,N}, para almacenar las velocidades vi(tk)=(vxi(tk),vyi(tk),vzi(tk)).

#4) Desde tk moverse en los datos al tiempo tk+t.

#5) Loop sobre i=1...N, los N atomos para leer vi(tk+t) y acumular en la suma
#fav(t)+=[vi(tk+t)*vi(tk)]^2.

#6) Volver al inicio de los datos y al paso (1) hasta barrer todos los t.

#----------------------------------------------------------------------------
#Preeliminares:
#----------------------------------------------------------------------------

f=open("output_difusion_sorted.lammpstrj")
lines=f.readlines()


#Numero de particulas
Numpart=int(lines[3])

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
timestep=[]
lookup = 'ITEM: ATOMS id type x y z vx vy vz'
k=0

with open("output_difusion_sorted.lammpstrj") as myFile:
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
#Funcion de autocorrelacion de las velocidades.
#-----------------------------------------------------------------------------

favx=np.zeros(len(timestep))
favy=np.zeros(len(timestep))
favz=np.zeros(len(timestep))
favtotal=np.zeros(len(timestep))

g=open('output_difusion_fav.txt','w')
g.write('time-step   fav_x fav_y fav_z fav_total \n')


for tdelay in range(0,len(timestep)-100):
    suma_x=0
    suma_y=0
    suma_z=0
    for torigin in range(0,len(timestep)-tdelay):
        for n in range(0,Numpart):
            if int(lines[datastart[torigin]+n].split(' ')[1])==1:  #id 1:Neutrones 2:Protones
                vxorigin= float(lines[datastart[torigin]+n].split(' ')[5])
                vxdelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[5])
                vyorigin= float(lines[datastart[torigin]+n].split(' ')[6])
                vydelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[6])
                vzorigin= float(lines[datastart[torigin]+n].split(' ')[7])
                vzdelay=  float(lines[datastart[torigin+tdelay]+n].split(' ')[7])
                dvx=vxdelay*vxorigin
                dvy=vydelay*vyorigin
                dvz=vzdelay*vzorigin
                suma_x+=dvx
                suma_y+=dvy
                suma_z+=dvz
    favx[tdelay]=suma_x/(Numpart*(len(timestep)-tdelay)) #promedio en part y en tiempo
    favy[tdelay]=suma_y/(Numpart*(len(timestep)-tdelay))
    favz[tdelay]=suma_z/(Numpart*(len(timestep)-tdelay))
    favtotal[tdelay]=favx[tdelay]+favy[tdelay]+favz[tdelay]
    g.write(str(tdelay)+' '+str(favx[tdelay])+' '+str(favy[tdelay])+' '+str(favz[tdelay])+' '+str(favtotal[tdelay])+'\n')
    print 'Done with tdelay '+str(tdelay)+'\n'

g.close()
