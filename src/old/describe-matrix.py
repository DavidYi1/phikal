import numpy as np 

import matplotlib.pyplot as plt 
import Graphics as artist

from sys import argv
from awesome_print import ap 
from matplotlib import rcParams

rcParams['text.usetex'] = True
filename = argv[1]

drugs = open('../data/master-drug-list','rb').read().splitlines()
m = np.loadtxt('../data/%s-matrix.tsv'%filename,delimiter='\t')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(m.ravel(),histtype='stepfilled',color='k',alpha=0.7)
artist.adjust_spines(ax)
ax.set_xlabel(artist.format(filename))
plt.yscale('log', nonposy='clip')
plt.tight_layout()
plt.savefig('../imgs/%s-matrix-distribution.png'%filename)

cutoff = np.percentile(m,85)
popular_combinations = {'%s-%s'%(one,two): m[i,j]
							for i,one in enumerate(drugs)
							for j,two in enumerate(drugs) 
							if m[i,j] > cutoff and j<i}

ap(sorted(popular_combinations.items(),key=lambda item:item[1],reverse=True))