#Plot of Dielectric Function from shell script output
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


data=np.loadtxt("optics.dat")

#Get the .dat file from the vasprun.xml using the shell script

#ipp approximation:
#awk 'BEGIN{i=1} /<imag>/, /<\/imag>/ {a[i]=$2 ; b[i]=$3 ; i=i+1} END{for (j=12;j<i-3;j++) print a[j],b[j]}' vasprun.xml > imag.dat
#awk 'BEGIN{i=1} /<real>/, /<\/real>/ {a[i]=$2 ; b[i]=$3 ; i=i+1} END{for (j=12;j<i-3;j++) print a[j],b[j]}' vasprun.xml > real.dat

#rpa approximation (first script is for ipa and the second is for rpa):
#awk 'BEGIN{i=0} /HEAD OF MICRO/, /<\/dielectricfunction>/ {if ($1=="<r>") {a[i]=$2 ; b[i]=($3+$4+$5)/3 ; i=i+1}} END{for (j=0;j<i/2;j++) print a[j],b[j],b[j+i/2]}' vasprun.xml > dielectric_ipa_varprunxml.dat
#awk 'BEGIN{i=0} /INVERSE MACRO/, /<\/dielectricfunction>/ {if ($1=="<r>") {a[i]=$2 ; b[i]=($3+$4+$5)/3 ; i=i+1}} END{for (j=0;j<i/2;j++) print a[j],b[j],b[j+i/2]}' vasprun.xml > dielectric_rpa_vasprunxml.dat
#output format: Energy (eV) Imaginary Real

#GW-BSE:
#awk 'BEGIN{i=0} /<dielectricfunction>/, /<\/dielectricfunction>/ {if ($1=="<r>") {a[i]=$2 ; b[i]=($3+$4+$5)/3 ; i=i+1}} END{for (j=0;j<i/2;j++) print a[j],b[j],b[j+i/2]}' vasprun.xml > optics.dat
#output format: Energy (eV) Imaginary Real

df = pd.DataFrame(data, columns=['Energy (eV)', 'Imaginary', 'Real'])
#print(df)

#plotting

fig, ax = plt.subplots(figsize=(5,4))
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", direction="in")
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax.tick_params(which='both', width=1, color='black', direction='in')
ax.tick_params(which='major', length=8)
ax.tick_params(which='minor', length=4)

plt.ylim([-4.0, 68.0])
plt.xlim([-0.5, 10.5])
plt.xticks(fontsize=15, fontname='Arial')
plt.yticks(fontsize=15, fontname='Arial')

plt.xlabel("Energy (eV)", fontsize=12, color='Black', fontname='Arial', fontweight='bold')
plt.ylabel(r"Dielectric Function ($\mathbf{\epsilon}$)", fontsize=12, color='Black', fontname='Arial', fontweight='bold')


plt.plot(df['Energy (eV)'], df['Imaginary'], ls='-', color='red', lw=1.5)
