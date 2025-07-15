#Plot of Bandstructure using GW+Wannier90

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

######################plotting######################################

fig, ax = plt.subplots(figsize=(4,5))
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", direction="in")
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))

ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', length=5, color='black', direction="in")

plt.xlabel("")
plt.ylabel("")

plt.yticks(fontsize=15, fontname='Arial')
plt.xticks(fontsize=15, fontname='Arial')
#plt.xticks([])
#ax.set_xticklabels([])


########################data processing##########################
data_band = np.loadtxt("wannier90_band.dat")
with open("wannier90_band.labelinfo.dat", "r") as f1:
    data_kp=f1.readlines()

with open("DOSCAR", "r") as f2:
    density_of_states_data=f2.readlines()
    Ef=float(density_of_states_data[5].split()[3])

high_sym_symbols=[]
num_kpts =[]
high_sym_points=[]
for info in data_kp:
    sym_symbols = info.split()[0]
    high_sym_symbols.append(sym_symbols)
    num_kpoints = info.split()[1]
    num_kpts.append(num_kpoints)
    sym_points = info.split()[2]
    high_sym_points.append(sym_points)

high_sym_points=list(map(float, high_sym_points)) #convert each memebr of the list from string to float
num_kpts = list(map(int, num_kpts)) #convert each memebr of the list from string to integer

###########################data extraction##################################
num_kp=num_kpts[-1]
xlim=high_sym_points[-1]  

Ene = data_band[:, 1] - Ef
nbands = int(len(Ene) / num_kp)
kp = data_band[:,0]

for i in range(nbands):
    energy = Ene[(i*num_kp):(i+1)*num_kp]
    kpoint = kp[(i*num_kp):(i+1)*num_kp]
    plt.plot(kpoint, energy, ls='-', color='red', lw=2)
    
ymin = -4.4
ymax = 4.4
plt.vlines(x=high_sym_points[1:-1], color='blue', linestyle='--', linewidth=1, ymin=ymin, ymax=ymax)   
plt.hlines(y=0, color='green', linestyle='--', linewidth=1, xmin=0, xmax=xlim)

plt.xlim(0, xlim)
plt.ylim(ymin, ymax)
plt.xticks(high_sym_points, high_sym_symbols)

