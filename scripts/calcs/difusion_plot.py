import numpy as np
import math as m
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------
#difusion_plot.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma los archivos de densidades out_densidades_Z
#y out_densidades_N y realiza dos graficos uno para protones y otro para
#neutrones mostrando la densidades a lo largo de pasos temporales elegidos
# por el usuario en el vector timestep=[,,].
#Ademas grafica el MSD, FAV, y D


#Author by Tavella Franco y Longo Lucas
#----------------------------------------------------------------------------

#Densidad de protones y neutrones
f=open("output_difusion_sorted.lammpstrj",'r')
lines=f.readlines()
#Numero de particulas
Numpart=int(lines[3])
f.close()

f=open("out_densidades_Z.txt",'r')
g=open("out_densidades_N.txt",'r')

linesZ=f.readlines()
linesN=g.readlines()

Numcels=int(linesZ[1].split(' ')[1])

#Recorro y encuentro los lugares donde empiezan los datos y me los guardo.
datastart=[]
dataend=[]
lookup = 'TIMESTEP: '

with open("out_densidades_Z.txt") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            datastart.append(num+1)
            dataend.append(num+Numcels)


#Extraemos los datos
#Z y N son dos diccionarios, cada lugar es un tiempo de la evolucion, y contiene una lista de [zposicion,densidad]
Z={}
N={}

for t in range(0,len(datastart)):
    zposicion=np.zeros(Numcels)
    densidadZ=np.zeros(Numcels)
    densidadN=np.zeros(Numcels)
    
    for l in range(0,Numcels):
        zposicion[l]=float(linesZ[l+datastart[t]].split(' ')[0])
        densidadZ[l]=float(linesZ[l+datastart[t]].split(' ')[1])
        densidadN[l]=float(linesN[l+datastart[t]].split(' ')[1])
        
    Z[t]=[zposicion,densidadZ]
    N[t]=[zposicion,densidadN]
    #print 'Done with timestep '+str(t)
    
f.close()
g.close()
#------------------------------------------------------------------------------
#MSD and D: Mean square displacement and Diffusion Coeficient

h=open('output_difusion_msd.txt')
lines=h.readlines()
MSD=[]

for i in range(1,len(lines)):
 MSD.append([int(lines[i].split(' ')[0]),float(lines[i].split(' ')[1]),float(lines[i].split(' ')[2])])

h.close()
#------------------------------------------------------------------------------
#FAV: Autocorrelation velocities function
h=open('output_difusion_fav.txt')
lines=h.readlines()
FAVX={}
FAVY={}
FAVZ={}
FAVtotal={}
times=[]
favx=[]
favy=[]
favz=[]
favtotal=[]
for i in range(1,len(lines)):
 times.append(lines[i].split(' ')[0])
 favx.append(lines[i].split(' ')[1])
 favy.append(lines[i].split(' ')[2])
 favz.append(lines[i].split(' ')[3])
 favtotal.append(lines[i].split(' ')[4])
FAVX[0]=times
FAVX[1]=favx
FAVY[0]=times
FAVY[1]=favy
FAVZ[0]=times
FAVZ[1]=favz
FAVtotal[0]=times
FAVtotal[1]=favtotal
h.close()
#------------------------------------------------------------------------------
#Graficos
#------------------------------------------------------------------------------
colordata=['bo','go','ro','co','mo','yo','ko','bo','go','ro','co','mo','yo','ko']
colorline=['b','g','r','c','m','y','k']
k=0

timestep=[1, 20, 40, 60, 80]#elijo los que quiero graficar
#Densidad Protones
plt.figure(1)
for g in timestep:
    plt.plot(Z[g][0],Z[g][1],colordata[k])
    plt.plot(Z[g][0],Z[g][1],colorline[k],label='step'+str(g))
    k=k+1

plt.title('Densidad Protones')
plt.xlabel('z')
plt.ylabel('rho_Z')
plt.legend(loc='lower right', numpoints=1)


#Densidad Neutrones
k=0
plt.figure(2)
for g in timestep:
    plt.plot(N[g][0],N[g][1],colordata[k])
    plt.plot(N[g][0],N[g][1],colorline[k],label='step'+str(g))
    k=k+1
    
plt.title('Densidad Neutrones')
plt.xlabel('z')
plt.ylabel('rho_N')
plt.legend(loc='lower right', numpoints=1)


#MSD(Mean Square Displacement)

plt.figure(3)
for g in range(0,len(MSD)):
 plt.plot((MSD[g][0]),(MSD[g][1]),'bo')
 plt.plot((MSD[g][0]),(MSD[g][1]),'b')
plt.title('Medium Square Displacement')
plt.xlabel('time-step')
plt.ylabel('MSD')

#Difusion
plt.figure(4) 
for g in range(1,len(MSD)):
 plt.plot(MSD[g][0],MSD[g][2],'go')
 plt.plot(MSD[g][0],MSD[g][2],'g')
plt.title('Coeficiente de Difusion')
plt.xlabel('time-step')
plt.ylabel('D')

#FAV
plt.figure(5)

plt.plot(FAVX[0],FAVX[1],colordata[1])
plt.plot(FAVX[0],FAVX[1],colorline[1],label='favx')
plt.plot(FAVX[0],FAVY[1],colordata[2])
plt.plot(FAVX[0],FAVY[1],colorline[2],label='favy')
plt.plot(FAVX[0],FAVZ[1],colordata[3])
plt.plot(FAVX[0],FAVZ[1],colorline[3],label='favz')
plt.plot(FAVtotal[0],FAVtotal[1],colordata[4])
plt.plot(FAVtotal[0],FAVtotal[1],colorline[4],label='favtotal')
 
plt.title('Funcion de autocorrelacion de velocidades')
plt.xlabel('time-step')
plt.ylabel('FAV')
plt.legend(loc='upper right')

plt.show()


