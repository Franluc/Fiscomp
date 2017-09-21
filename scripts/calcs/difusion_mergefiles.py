#----------------------------------------------------------------------------
#difusion_mergefiles.py:
#----------------------------------------------------------------------------
#El siguiente archivo toma los archivos de salida de dos celdas ZN y NN y los
#une en unica celda del doble de tamano con las configuraciones finales de
#cada una de las celdas. Luego se utilizaran como input para recrear la
#condiciones inicial en lammps.
#
#Author by Tavella Franco y Longo Lucas
#------------------------------------------------------------------

fileNN = open('output_3000_NN.lammpstrj', 'r')
fileZN = open('output_3000_ZN.lammpstrj', 'r')
linesNN=fileNN.readlines()
linesZN=fileZN.readlines()

N=int(linesNN[3]) #NUMBER OF ATOMS IN ONE SLUB
#NEW BOX DIMENSIONS
xlo=float(linesNN[5].split(' ')[0])#xlo
xhi=float(linesNN[5].split(' ')[1])#xhi
ylo=float(linesNN[6].split(' ')[0])#ylo
yhi=float(linesNN[6].split(' ')[1])#yhi
zlo=float(linesNN[7].split(' ')[0])#zlo
zhi=2*float(linesNN[7].split(' ')[1])#zhi

#SLAB 1 NN
numblinesNN=len(linesNN)#NUMBER OF LINES IN FILE    
fileNN.close()


#SLAB 2 NP
numblinesZN=len(linesZN)#NUMBER OF LINES IN FILE  
fileZN.close()


#CREATE FILE

f=open('data.input_ZNyN','w')
f.write('#Lammps input data by Longo Lucas and Tavella Franco\n')
f.write('\n')
f.write(str(2*N)+' '+'atoms\n')
f.write('\n')
f.write(str(2)+' '+'atom types\n')
f.write('\n')
f.write(str(xlo)+' '+str(xhi)+' '+'xlo'+' '+'xhi\n')
f.write(str(ylo)+' '+str(yhi)+' '+'ylo'+' '+'yhi\n')
f.write(str(zlo)+' '+str(zhi)+' '+'zlo'+' '+'zhi\n')
f.write('\n')
f.write('Masses\n')
f.write('\n')
f.write(str(1)+' '+str(938.0)+'\n')
f.write(str(2)+' '+str(938.0)+'\n')
f.write('\n')
f.write('Atoms'+' '+'#atom_ID atom_type x y z\n')
f.write('\n')
#LASTS SNAPSHOT
for i in range(0,N):
 atomid=i+1
 atomtype=int(linesNN[numblinesNN-(i+1)].split(' ')[1])
 x=float(linesNN[numblinesNN-(i+1)].split(' ')[2])
 y=float(linesNN[numblinesNN-(i+1)].split(' ')[3])
 z=float(linesNN[numblinesNN-(i+1)].split(' ')[4])     
 f.write(str(atomid)+' '+str(atomtype)+' '+str(x)+' '+str(y)+' '+str(z)+'\n')

for i in range(0,N):
 atomid=i+1+N
 atomtype=int(linesZN[numblinesZN-(i+1)].split(' ')[1])
 x=float(linesZN[numblinesZN-(i+1)].split(' ')[2])
 y=float(linesZN[numblinesZN-(i+1)].split(' ')[3])
 z=float(linesZN[numblinesZN-(i+1)].split(' ')[4])+(zhi/2)#traslacion en z
 f.write(str(atomid)+' '+str(atomtype)+' '+str(x)+' '+str(y)+' '+str(z)+'\n')

f.write('\n')
f.write('Velocities' +' '+'#atom_ID vx vy vz\n')
f.write('\n')
for i in range(0,N):
 atomid=i+1
 vx=float(linesNN[numblinesNN-(i+1)].split(' ')[5])
 vy=float(linesNN[numblinesNN-(i+1)].split(' ')[6])
 vz=float(linesNN[numblinesNN-(i+1)].split(' ')[7])     
 f.write(str(atomid)+' '+str(vx)+' '+str(vy)+' '+str(vz)+'\n')

for i in range(0,N):
 atomid=i+1+N
 vx=float(linesZN[numblinesZN-(i+1)].split(' ')[5])
 vy=float(linesZN[numblinesZN-(i+1)].split(' ')[6])
 vz=float(linesZN[numblinesZN-(i+1)].split(' ')[7])
 f.write(str(atomid)+' '+str(vx)+' '+str(vy)+' '+str(vz)+'\n')

f.close()


