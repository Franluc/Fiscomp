import numpy as np
import math as m
import matplotlib.pyplot as plt


#----------------------------------------------------------------------------
#difusion_truepositions.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma cada timestep en el archivo output_difusion_sorted
#y realiza el calculo de las posiciones verdaderas(sin condiciones periodicas
#de contorno)para luego aplicar el algoritmo que calcula el MSD.


#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------

f=open('output_difusion_sorted.lammpstrj')
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

L_x = xhi - xlo # Box x size
L_y = yhi - ylo # Box y size
L_z = zhi - zlo # Box z size

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
timestep=[]
lookup = 'ITEM: ATOMS id type x y z vx vy vz '
lookup2= 'ITEM: TIMESTEP'
with open('output_difusion_sorted.lammpstrj') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart.append(num)
            dataend.append(num+Numpart-1)
       

with open('output_difusion_sorted.lammpstrj') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup2 in line:
            timestep.append(int(lines[num]))           


#Extraigo los x,y,z de las particulas y les aplico la correccion: X{} contiene 6000 arrays, cada uno con la posicion verdadera en x de la particula i en funcion del tiempo(timesteps)
Xtrue={}
Vx={}
Ytrue={}
Vy={}
Ztrue={}
Vz={}
idtype=[]

for n in range(0,Numpart):
 idtype.append(lines[datastart[0]+n].split(' ')[1])
for n in range(0,Numpart):   
 Xpart=np.zeros(len(datastart))
 Ypart=np.zeros(len(datastart))
 Zpart=np.zeros(len(datastart))
 Vxpart=np.zeros(len(datastart))
 Vypart=np.zeros(len(datastart))
 Vzpart=np.zeros(len(datastart))
 for i in range(0,len(datastart)):
  Xpart[i]=float(lines[datastart[i]+n].split(' ')[2])
  Ypart[i]=float(lines[datastart[i]+n].split(' ')[3])
  Zpart[i]=float(lines[datastart[i]+n].split(' ')[4])
  Vxpart[i]=float(lines[datastart[i]+n].split(' ')[5])
  Vypart[i]=float(lines[datastart[i]+n].split(' ')[6])
  Vzpart[i]=float(lines[datastart[i]+n].split(' ')[7])
 for i in range(0,len(Xpart)-1):
  xold=Xpart[i]/L_x
  yold=Ypart[i]/L_y
  zold=Zpart[i]/L_z
  xnew=Xpart[i+1]/L_x
  ynew=Ypart[i+1]/L_y
  znew=Zpart[i+1]/L_z
  dxfalse=xnew-xold
  dyfalse=ynew-yold
  dzfalse=znew-zold
  dxtrue=dxfalse-int(round(dxfalse))
  dytrue=dyfalse-int(round(dyfalse))
  dztrue=dzfalse-int(round(dzfalse))
  Xpart[i+1]=(xold+dxtrue)*L_x
  Ypart[i+1]=(yold+dytrue)*L_y
  Zpart[i+1]=(zold+dztrue)*L_z 
  # Si la diferencia es mayor a L/2 es que hubo correccion por C.C.
  #if(dx < -L_x/2):
  #    Xpart[i+1] = xnew + L_x
  #elif(dx > L_x/2):
  #    Xpart[i+1] = xnew - L_x
  #if(dy < -L_y/2):
  #    Ypart[i+1] = ynew + L_y
  #elif(dy > L_y/2):
  #    Ypart[i+1] = ynew - L_y
  #if(dz < -L_z/2):
  #    Zpart[i+1] = znew + L_z
  #elif(dz > L_z/2):
  #    Zpart[i+1] = znew - L_z     
 Xtrue[n]=Xpart
 Vx[n]=Vxpart
 Ytrue[n]=Ypart
 Vy[n]=Vypart
 Ztrue[n]=Zpart
 Vz[n]=Vzpart


#Imprimo nuevo archivo con las posiciones verdaderas
g=open('output_difusion_sorted_true.lammpstrj','w')
for i in range(0,len(datastart)):
     g.write('ITEM: TIMESTEP\n')
     g.write(str(timestep[i])+'\n')
     g.write('ITEM: NUMBER OF ATOMS\n')
     g.write(str(Numpart)+'\n')
     g.write('ITEM: BOX BOUNDS pp pp pp\n')
     g.write(str(xlo)+' '+str(xhi)+'\n')
     g.write(str(ylo)+' '+str(yhi)+'\n')
     g.write(str(zlo)+' '+str(zhi)+'\n')
     g.write('ITEM: ATOMS id type x y z vx vy vz\n')
     for n in range(0,Numpart):
         g.write(str(n+1)+' '+str(idtype[n])+' '+str(Xtrue[n][i])+' '+str(Ytrue[n][i])+' '+str(Ztrue[n][i])+' '+str(Vx[n][i])+' '+str(Vy[n][i])+' '+str(Vz[n][i])+'\n')

g.close()


