import json 

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist
import utils as tech 

from matplotlib import rcParams
rcParams['text.usetex'] = True
READ = 'rb'
drugs = open('master-drug-list',READ).read().splitlines()

m = np.loadtxt('comention-matrix.tsv',delimiter='\t').astype(int)

cutoff = 20
labels,freqs = zip(*sorted(zip(drugs,np.diag(m)), key=lambda item:item[1],reverse=True)[:cutoff])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs,'k--',linewidth=2)
artist.adjust_spines(ax)
ax.set_xticks(range(len(freqs)))
ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
plt.tight_layout()
plt.show()