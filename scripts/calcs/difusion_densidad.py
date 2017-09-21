import numpy as np
import math as m
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#difusion_densidad.py:
#----------------------------------------------------------------------------
#El siguiente archivo realiza un grillado en 3 dimensiones de toda la celda.
#Luego calcula las densidades tanto para protones(Z) como para neutrones(N) a
#a lo largo de la direccion z. Luego imprime dos archivos out_densidades_Z y
#out_densidades_N con una tabla Z vs densidad para cada tiempo:
# Z vs densidad
# x      x
# x      x
# x      x

#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------

#Densidad de protones
f=open("output_difusion_sorted.lammpstrj")
lines=f.readlines()
#Dimensiones de la celda grande
xlo=lines[5].split(' ')[0]
xhi=lines[5].split(' ')[1]
ylo=lines[6].split(' ')[0]
yhi=lines[6].split(' ')[1]
zlo=lines[7].split(' ')[0]
zhi=lines[7].split(' ')[1]

#Numero de particulas
Numpart=int(lines[3])

#Dividimos toda la celda en celdas de lXlXl:
Numcels=20
#largo de una de las celditas
L=float(xhi)
l=float(L/Numcels)

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
lookup = 'ITEM: ATOMS id type x y z vx vy vz '

with open("output_difusion_sorted.lammpstrj") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart.append(num)
            dataend.append(num+Numpart-1)

#Archivos para salida de datos
g=open('out_densidades_Z.txt','w')
h=open('out_densidades_N.txt','w')
g.write('DENSIDADES PROTONES\n')
h.write('DENSIDADES NEUTRONES\n')
g.write('NUMCELS '+str(Numcels)+'\n')
h.write('NUMCELS '+str(Numcels)+'\n')

for t in range(0,len(datastart)):
    g.write('TIMESTEP: '+str(t)+'\n')
    h.write('TIMESTEP: '+str(t)+'\n')
    g.write('z densidad\n')
    h.write('z densidad\n')
#Recorremos el archivo y donde encuentro un proton/neutron que incremente la cuenta de esa celda en la matriz correspondiente: Z(matriz de protones) y N(matriz de neutrones)
    Z=np.zeros((Numcels,Numcels,Numcels),dtype=int)
    N=np.zeros((Numcels,Numcels,Numcels),dtype=int)
    for i in range(datastart[t],dataend[t]):
        #Me fijo en que celda se encuentra
        x=float(lines[i].split(' ')[2])
        y=float(lines[i].split(' ')[3])
        z=float(lines[i].split(' ')[4])

        #Condiciones periodicas

        xcp=float(lines[i].split(' ')[2])-L*m.floor(x/L)
        ycp=float(lines[i].split(' ')[3])-L*m.floor(y/L)
        zcp=float(lines[i].split(' ')[4])-L*m.floor(z/L)
        
        #Celda
        numxcelda=m.floor(xcp/l)
        numycelda=m.floor(ycp/l)
        numzcelda=m.floor(zcp/l)
            
        if float(lines[i].split(' ')[1]) == 2: #ID 1:NEUTRONES 2:PROTONES
            #print 'Es proton'
            #Incremento el numero de la celda (numxcelda, numycelda, numzcelda) en Z
            oldcount=Z[int(numzcelda)][int(numxcelda)][int(numycelda)]
            newcount=oldcount+1
            Z[int(numzcelda)][int(numxcelda)][int(numycelda)]=newcount    
        else:
            #print 'No proton'
            #Incremento el numero de la celda (numxcelda, numycelda, numzcelda) en N
            oldcount=N[int(numzcelda)][int(numxcelda)][int(numycelda)]
            newcount=oldcount+1
            N[int(numzcelda)][int(numxcelda)][int(numycelda)]=newcount 

        #Ahora calculamos por cada capa en la direccion z solamente
        zposicion=np.zeros(Numcels,dtype=float)
        densidadZ=np.zeros(Numcels,dtype=float)
        densidadN=np.zeros(Numcels,dtype=float)
    for j in range(0,Numcels):
        vol=L*L*l #volumen de una de las celdas de LxLxl
        zposicion[j]=j*l
        densidadZ[j]=np.sum(Z[j])/vol
        densidadN[j]=np.sum(N[j])/vol
        g.write(str("%.2f" % zposicion[j])+' '+str("%.4f" % densidadZ[j])+'\n')
        h.write(str("%.2f" % zposicion[j])+' '+str("%.4f" % densidadN[j])+'\n')
            
        #Guardo en el diccionario
    g.write('\n')
    h.write('\n')
    print 'Done with timestep '+str(t)

g.close()
h.close()


               
