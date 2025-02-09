#Calculation of band gap of the material using GGA_PBE functional

import numpy as np


#########Reading OUTCAR and EIGENVAL files######################
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
    kpoint_coords = [float(x) for x in data[line_index].split()[:3]]
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
        ene=[item for e in energies[k] for item in e]
        energy_result.append(ene)
    else:
        ene=energies[k]
        energy_result.append(ene)

kpoints = np.array(kpoints)
energies = np.array(energy_result)

energies = (energies - Ef)
xaxis = [l for l in range(len(kpoints))]

kp_ene=list(zip(kpoints, energies))
########## seperate vbm and cbm #######################
occupied=[]
unoccupied=[]
for m in kp_ene:
    occ=(m[0], [O for O in m[1] if O < 0.05]) #sometimes vbm bands cross slighly the Fermi energy
    unocc=(m[0], [U for U in m[1] if U > 0.05]) #sometimes cbm bands cross slightly the Fermi energy
    occupied.append(occ)
    unoccupied.append(unocc)
    
vbm_bands=[]
for o in range(len(occupied)):
    vbm_result=len(occupied[o][1])
    vbm_bands.append(vbm_result)

cbm_bands=[]
for p in range(len(unoccupied)):
    cbm_result=len(unoccupied[p][1])
    cbm_bands.append(cbm_result)

number_of_bands_considered_vbm_side=min(vbm_bands)  #To have symmetric matrix 
number_of_bands_considered_cbm_side=min(cbm_bands)  #To have symmetric matrix

vbm_kpoints=[]
vbm_energies=[]
for q in occupied:
    vbm_kp=q[0]
    vbm_kpoints.append(vbm_kp)
    vbm_ene=q[1]
    vbm_ene=vbm_ene[::-1]
    vbm_ene=vbm_ene[:(number_of_bands_considered_vbm_side)]
    vbm_energies.append(vbm_ene)
cbm_kpoints=[]
cbm_energies=[]
for r in unoccupied:
    cbm_kp=r[0]
    cbm_kpoints.append(cbm_kp)
    cbm_ene=r[1][:(number_of_bands_considered_cbm_side)]
    cbm_energies.append(cbm_ene)
#########################Calculation of band gap############################
max_vbm_energy_each_kp=[[] for s in vbm_energies]
for t in range(len(vbm_energies)):
    max_vbm_energy_each_kp[t].append(max(vbm_energies[t]))

min_cbm_energy_each_kp=[[] for u in cbm_energies]
for v in range(len(cbm_energies)):
    min_cbm_energy_each_kp[v].append(min(cbm_energies[v]))

vbm_kp_index=max_vbm_energy_each_kp.index(max(max_vbm_energy_each_kp))
vbm=max(max_vbm_energy_each_kp)
kp_of_vbm=vbm_kpoints[vbm_kp_index]

cbm_kp_index=min_cbm_energy_each_kp.index(min(min_cbm_energy_each_kp))
cbm=min(min_cbm_energy_each_kp)
kp_of_cbm=cbm_kpoints[cbm_kp_index]

##################################Results#####################
for a, b in zip(vbm, cbm):
    band_gap=round((b-a), 2)
    a=round(a, 2)
    b=round(b, 2)
    print(f'VBM is located at {a} and kpoint is {kp_of_vbm}. CBM is located at {b} and the kpoint is {kp_of_cbm}. The band gap of the material is {band_gap}')

    
flag = all(x == y for x, y in zip(kp_of_vbm, kp_of_cbm))
if flag:
    print("The material has direct band gap")
else:
    print("The material has indirect band gap")
#reference=https://aflowlib.org/material/?id=72832
