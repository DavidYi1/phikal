import json 

import numpy as np 
import matplotlib.pyplot as plt
import Graphics as artist

from  matplotlib import rcParams
rcParams['text.usetex'] = True

m = np.loadtxt('../data/drug-matrix-actually-occurred.tsv',delimiter='\t').astype(int)
m += 1
m /= 2 

db = json.load(open('../data/db.json','rb'))


fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(m.sum(axis=0),color='k',alpha=0.7)
artist.adjust_spines(ax)
ax.set_xlabel(artist.format('No. of mentions'))
ax.set_ylabel(artist.format('Frequency'))
#plt.yscale('log', nonposy='clip')
plt.tight_layout()
plt.savefig('../imgs/drug-frequency-log.png')

'''
freqs = [len(db[entry]["drugs"]) for entry in db]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(freqs,color='k',alpha=0.7)
artist.adjust_spines(ax)
ax.set_xlabel(artist.format('No. of drugs'))
ax.set_ylabel(artist.format('No. of documents'))
plt.tight_layout()
plt.savefig('../imgs/distribution-of-drugs-across-docs.png')
'''