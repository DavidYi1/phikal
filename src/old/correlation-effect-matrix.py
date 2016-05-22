import numpy as np 

import Graphics as artist
import matplotlib.pyplot as plt 

from matplotlib import rcParams
rcParams['text.usetex'] = True

m = np.loadtxt('../data/effect-matrix.tsv')

xm = m.dot(m.T)
xm /= m.shape[1]

np.savetxt('../data/effect-correlation-matrix.tsv', xm,fmt='%d',delimiter='\t')

fig = plt.figure()
ax = fig.add_subplot(111)
cax=ax.imshow(xm,interpolation='nearest',aspect='auto',cmap=plt.cm.seismic,
	vmin=-1,vmax=1)
artist.adjust_spines(ax,[])
ax.set_xlabel(artist.format('Effect'))
ax.set_ylabel(artist.format('Effect'))
plt.colorbar(cax)
plt.tight_layout()
plt.savefig('../imgs/effect-correlation-matrix.png')