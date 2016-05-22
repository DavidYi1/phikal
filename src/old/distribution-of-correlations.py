import json 

import numpy as np 

import Graphics as artist
import matplotlib.pyplot as plt

from awesome_print import ap 
from matplotlib import rcParams
rcParams['text.usetex'] = True

clusters = json.load(open("drugs-in-each-cluster.json",'rb'))

data = np.loadtxt('correlation-matrix.tsv',delimiter='\t')
drugs = open('master-drug-list').read().splitlines()

idx = {cluster:[i for i,drug in enumerate(drugs) 
			if drug in clusters[cluster]] 
			for cluster in clusters}

'''
fig,(both,cl1,cl2) = plt.subplots(ncols=3,sharex=True,sharey=True, figsize=(12,6))
both.hist(np.tril(data,k=-1).ravel(),range=(0,1),histtype='step',color='k')
artist.adjust_spines(both)
both.set_ylabel(artist.format('Correlation'))
both.set_xticks([0,0.5,1])

cl1.hist(np.tril(data,k=-1)[:,idx["0"]].ravel(),histtype='step', color='k')
artist.adjust_spines(cl1)
cl1.set_title(artist.format('Cluster 1'))
cl1.set_xticks([0,0.5,1])

cl2.hist(np.tril(data,k=-1)[:,idx["1"]].ravel(),histtype='step', color='k')
artist.adjust_spines(cl2)
cl2.set_title(artist.format('Cluster 2'))
cl2.set_xticks([0,0.5,1])
plt.tight_layout()
plt.show()
'''

options = {"histtype":"stepfilled","alpha":0.6,"range":(-1,1)}
fig = plt.figure()
ax = fig.add_subplot(111)
for values,color,name in zip([np.tril(data,k=-1).ravel(),
		np.tril(data,k=-1)[:,idx["0"]].ravel(),np.tril(data,k=-1)[:,idx["1"]].ravel() ],
		['k','r','b'],['All','Cluster 1',"Cluster 2"]):
	print np.count_nonzero(values),values.size
	ax.hist(values,label=artist.format(name),color=color,**options)
artist.adjust_spines(ax)
plt.legend(frameon=False)
plt.tight_layout()
plt.show()

