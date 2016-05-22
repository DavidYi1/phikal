import numpy as np 
import Graphics as artist
import matplotlib.pyplot as plt 
import matplotlib.ticker as plticker

from matplotlib import rcParams
rcParams['text.usetex'] = True 
READ = 'rb'
m = np.loadtxt('../data/drug-effect-matrix.tsv',delimiter='\t')
FX = open('../data/effects-that-actually-occurred',READ).read().splitlines()
drugs = open('../data/drugs-that-actually-occurr',READ).read().splitlines()
'''
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(m,interpolation='nearest',aspect='auto',cmap=plt.cm.bone_r)
artist.adjust_spines(ax)
ax.set_xlabel(artist.format('Effects'))
ax.set_ylabel(artist.format('Substances'))
cbar = plt.colorbar(cax)
cbar.set_label(artist.format('No. of mentions'))
cbar.locator = plticker.MultipleLocator(base=1000.0)
cbar.update_ticks()
plt.tight_layout()
plt.savefig('../imgs/drugs-v-effect.png')
'''

correction_factor = m.size
cutoff = 0.05 /correction_factor
print cutoff

#threshold = np.percentile(m.ravel(),100-cutoff)
threshold = 1000

for i,j in zip(*np.where(m>=threshold)):
	print drugs[i],FX[j]