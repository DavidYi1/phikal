import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist

from matplotlib import rcParams
rcParams['text.usetex'] = True

from sys import argv
filename = argv[1]

m = np.loadtxt('../data/%s-matrix.tsv'%filename,delimiter='\t')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(m,interpolation='nearest',aspect='auto',cmap=plt.cm.bone_r)

cbar = plt.colorbar(cax)
#cbar.set_ticks([0,0.25,0.5,0.75,1] if filename == 'jaccard' else
#			[-1,-.5,0,.5,1])
artist.adjust_spines(ax)
plt.tight_layout()
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('../imgs/%s-matrix.png'%filename)
