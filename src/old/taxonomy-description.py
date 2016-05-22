import numpy as np 
import Graphics as artist
import matplotlib.pyplot as plt 

from matplotlib import rcParams
rcParams['text.usetex'] = True

m = np.loadtxt('../data/taxonomy-matrix.tsv',delimiter='\t')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(np.tril(m).ravel(),color='k',histtype='stepfilled',alpha=0.6)
artist.adjust_spines(ax)
ax.set_xlabel(artist.format('No. of mentions'))
plt.yscale('log', nonposy='clip')
plt.tight_layout()
plt.show()