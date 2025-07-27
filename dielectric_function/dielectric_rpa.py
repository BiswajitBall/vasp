#Plot of Dielectric Function in the Random Phase Approximation (RPA)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

######output from vasprun.xml/OUTCAR using shell script#############
#awk 'BEGIN{i=1} /HEAD OF MICRO/, /XI_LOCAL/ {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' OUTCAR > dielectric_ipa_outcar.dat
#awk 'BEGIN{i=1} /INVERSE MACRO/, /XI_TO_W/ {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' OUTCAR > dielectric_rpa_outcar.dat
#output format from OUTCAR: Energy (eV) Real Imaginary

#awk 'BEGIN{i=0} /HEAD OF MICRO/, /<\/dielectricfunction>/ {if ($1=="<r>") {a[i]=$2 ; b[i]=($3+$4+$5)/3 ; i=i+1}} END{for (j=0;j<i/2;j++) print a[j],b[j],b[j+i/2]}' vasprun.xml > dielectric_ipa_varprunxml.dat
#awk 'BEGIN{i=0} /INVERSE MACRO/, /<\/dielectricfunction>/ {if ($1=="<r>") {a[i]=$2 ; b[i]=($3+$4+$5)/3 ; i=i+1}} END{for (j=0;j<i/2;j++) print a[j],b[j],b[j+i/2]}' vasprun.xml > dielectric_rpa_vasprunxml.dat
#output format from vasprun.xml: Energy (eV) Imaginary Real

# Read OUTCAR file
with open("OUTCAR", "r") as f:
    lines = f.readlines()

############## extract the lines between INVERSE MACROSCOPIC DIELECTRIC TENSOR and XI_TO_W ################
#extract lines between HEAD OF MICROSCOPIC DIELECTRIC TENSOR and XI_LOCAL to get the dielectric function in IPA#
#extract lines between HEAD OF INVERSE MACROSCOPIC DIELECTRIC TENSOR and XI_TO_W to get the dielectric function in RPA#

extract_line=False
block=[]

for line in lines:
    if "INVERSE MACROSCOPIC DIELECTRIC TENSOR" in line and "RPA" in line:
        extract_line=True
        continue
    if "XI_TO_W" in line:
        extract_line=False
        break
    if extract_line and 'dielectric' in line:
        block.append(line.replace('dielectric', '').replace('constant','').strip().split())

#string to float conversion
data=[]
for elem in block:
    result=list(map(float, elem))
    data.append(result)
#print(data)

##########################Create pandas dataframe#########################
df = pd.DataFrame(data, columns=['Energy (eV)', 'Real', 'Imaginary'])
#print(df)

###########plotting dielectric function#######################

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



plt.plot(df['Energy (eV)'], df['Imaginary'], ls='-', color='red', lw=1.5)
plt.plot(df['Energy (eV)'], df['Real'], ls='-', color='blue', lw=1.5)

#plt.title(f"Plot of Dielectric Function in the Random Phase Approximation (RPA)", fontweight='bold', fontsize=16)
