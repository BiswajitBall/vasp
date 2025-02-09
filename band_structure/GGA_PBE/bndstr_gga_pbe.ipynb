#Plot of electronic band structure using GGA-PBE functional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

#########Reading OUTCAR/DOSCAR and EIGENVAL files######################
# with open("OUTCAR_Cs2NbF6", "r") as f1:
#     lines = f1.readlines()
# for line in lines:
#     if "E-fermi" in line:
#         Ef=float(line.split()[2])
        
with open("DOSCAR_Cs2NbF6", "r") as f1:
    density_of_states_data=f1.readlines()
    Ef=float(density_of_states_data[5].split()[3])

with open('EIGENVAL_Cs2NbF6', 'r') as f2:
    data = f2.readlines()
    
############Extracting data from EIGENVAL########################
nelectrons=int(data[5].split()[0])
nkpts = int(data[5].split()[1])
nbands = int(data[5].split()[2])
ispin=int(data[0].split()[3])
natoms=int(data[0].split()[1])

##########Extracting kpoints and energy eigenvalues data#################
kpoints = []
energies = []
for i in range(nkpts):
    line_index = 7+(nbands+2)*i
    kpoint_coords = [float(x) for x in data[line_index].split()[:4]]
    eigenvalues = []
    for j in range(nbands):
        if ispin==1:
            eigenvalue= float(data[line_index+j+1].split()[1])
            energy_data=(eigenvalue)
        else:
            eigenvalue_up = float(data[line_index+j+1].split()[1])
            eigenvalue_down = float(data[line_index+j+1].split()[2])
            energy_data=(eigenvalue_up, eigenvalue_down)
        eigenvalues.append(energy_data)
    kpoints.append(kpoint_coords)
    energies.append(eigenvalues)
energy_result=[]
for k in range(len(energies)):
    if ispin==2:
        ene=[item for e in energies[k] for item in e]  #list of tuples to list 
        energy_result.append(ene)
    else:
        ene=energies[k]
        energy_result.append(ene)

kpoints = np.array(kpoints)
energies = np.array(energy_result)

energies = (energies - Ef)
xaxis = [l for l in range(len(kpoints))]
##########plotting band structure#######################

fig, ax = plt.subplots(figsize=(8,5))
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", direction="in")
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='both', width=1, color='black', direction='in')
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', length=4)


plt.ylim([-8.0, 8.0])
plt.xlim([xaxis[0], xaxis[-1]])


plt.xlabel("K-Points", fontsize=12, color='Black', fontname='Arial', fontweight='bold')
plt.ylabel("(E - Ef) (eV)", fontsize=12, color='Black', fontname='Arial', fontweight='bold')

for m in range(nbands):
    if (ispin==2):
        energies_up=energies[:, ::2]
        energies_down=energies[:, 1::2]
        plt.plot(xaxis, energies_up[:, m], color="red", ls="-", lw=1) #up_spin
        plt.plot(xaxis, energies_down[:, m], color="blue", ls="-", lw=1) #down_spin
    else:
        plt.plot(xaxis, energies[:, m], color="red", ls="-", lw=1)

kpath='G-Y-F-L-I|I1-Z-G-X|X1-Y|M-G-N|Z-F1' 
kp_symbols=kpath.split('-')
interval=int((len(kpoints))/(len(kp_symbols)-1))
xaxis_kp_symbols=[xaxis[0]]+[xaxis[n] for n in range(interval, len(xaxis), interval)]+[xaxis[-1]]



plt.xticks(xaxis_kp_symbols, kp_symbols, fontsize=12, fontname='Arial')
plt.axhline(y=0, color='green', linestyle='--', lw=1.5)

for ver_line in range(len(kp_symbols)):
    plt.axvline(x=xaxis_kp_symbols[ver_line], color='grey', linestyle='--', lw=1)

material_name='Cs2NbF6'
#reference=https://aflowlib.org/material/?id=72832
plt.title(f"Electronic Band Structure Plot of {material_name} using GGA-PBE Functional", fontweight='bold', fontsize=16)
#plt.savefig('bndstr.png', dpi=800)
plt.show()
