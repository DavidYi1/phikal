import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist

from matplotlib import rcParams
rcParams['text.usetex'] = True

m = np.loadtxt('correlation-matrix.tsv',delimiter='\t')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(m,interpolation='nearest',aspect='auto',cmap=plt.cm.bone_r,vmin=-1,vmax=1)
artist.adjust_spines(ax)
plt.colorbar(cax)
plt.show()