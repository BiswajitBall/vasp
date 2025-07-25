#Plot of Dielectric Function in the Independent Particle Approximation (IPA)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Read OUTCAR file
with open("OUTCAR", "r") as f:
    lines = f.readlines()

##############Find the index where the imaginary and real dielectric blocks start################
imag_index = [i for i, line in enumerate(lines) if 'IMAGINARY DIELECTRIC FUNCTION' in line and 'density-density' in line]
real_index = [j for j, line in enumerate(lines) if 'REAL DIELECTRIC FUNCTION' in line and 'density-density' in line]

##################Extract imaginary part#######################
imag_data = []
imag_data_start_index = int(imag_index[0]) + 3
while imag_data_start_index < len(lines):
    imag_block = lines[imag_data_start_index].split()
    if len(imag_block) == 7:
        imag_data.append(list(map(float, imag_block)))
    else:
        break
    imag_data_start_index += 1
#print(imag_data)  

real_data = []
real_data_start_index = int(real_index[0]) + 3
while real_data_start_index < len(lines):
    real_block = lines[real_data_start_index].split()
    if len(real_block) == 7:
        real_data.append(list(map(float, real_block)))
    else:
        break
    real_data_start_index += 1
#print(real_data)    

##########################Create pandas dataframe#########################

imag_df = pd.DataFrame(imag_data, columns=['Energy (eV)', 'Im(e_xx)', 'Im(e_yy)', 'Im(e_zz)', 'Im(e_xy)', 'Im(e_yz)', 'Im(e_zx)'])
real_df = pd.DataFrame(real_data, columns=['Energy (eV)', 'Im(e_xx)', 'Im(e_yy)', 'Im(e_zz)', 'Im(e_xy)', 'Im(e_yz)', 'Im(e_zx)'])

#print(real_df)

##########plotting dielectric function#######################

fig, ax = plt.subplots(figsize=(5,4))
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", direction="in")
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax.tick_params(which='both', width=1, color='black', direction='in')
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', length=4)

plt.ylim([-6.0, 16.0])
plt.xlim([-10, 210])
plt.xticks(fontsize=15, fontname='Arial')
plt.yticks(fontsize=15, fontname='Arial')

plt.xlabel("Energy (eV)", fontsize=12, color='Black', fontname='Arial', fontweight='bold')
plt.ylabel(r"Dielectric Function ($\mathbf{\epsilon}$)", fontsize=12, color='Black', fontname='Arial', fontweight='bold')



plt.plot(imag_df['Energy (eV)'], imag_df['Im(e_xx)'], ls='-', color='red', lw=1.5)
plt.plot(real_df['Energy (eV)'], real_df['Im(e_xx)'], ls='-', color='blue', lw=1.5)

#plt.title(f"Plot of Dielectric Function in the Independent Particle Approximation (IPA)", fontweight='bold', fontsize=16)
