import json 

import matplotlib.pyplot as plt 
import Graphics as artist 
import numpy as np 
import utils as tech 

from collections import Counter
from matplotlib import rcParams
from awesome_print import ap 

rcParams['text.usetex'] = True
effects = json.load(open("../data/drugs-in-each-cluster-taxonomy.json",'rb'))
clusters = json.load(open("../data/taxonomy-matrix-kmeans-cluster-labels.json",'rb'))
taxonomy = json.load(open("../data/drug-taxonomy.json",'rb'))
drugs = open('../data/master-drug-list','rb').read().splitlines()

mentions = np.diag(np.loadtxt('../data/comention-matrix.tsv',delimiter='\t').astype(int))
nclus = 4

#What effects in each clusters
d = {}

d["drugs"] = {cluster:[drug for drug in taxonomy 
			if any([effect in effects[cluster] 
				for effect in taxonomy[drug]["effects"]])] 
				for cluster in effects}


d["class"] = {cluster:dict(Counter(list(tech.flatten([taxonomy[drug]["class"] 
				if "class" in taxonomy[drug] else taxonomy[drug]["effects"]
				for drug in taxonomy 
				if any([effect in effects[cluster] 
				for effect in taxonomy[drug]["effects"]])])))) 
				for cluster in effects}


d["unique"] = {}
for cluster in effects:
	keys = d["class"].keys()
	keys.remove(str(cluster))
	drug_list = list(set(d["drugs"][cluster]) - set(tech.flatten([d["drugs"][other]
											for other in keys])))
	d["unique"][cluster] = {drug:mentions[drugs.index(drug)] 
			for drug in drug_list
			if drug in drugs} #This last line is a hack. Escitaloprams wasn't in list

json.dump(d,open('effects-drugs-crosstab.json','wb'))

nrows = 2
ncols = 2
cutoff = 15
fig,axs = plt.subplots(nrows=nrows,ncols=ncols,figsize=(8,12))
for row in xrange(nrows):
	for col in xrange(ncols):
		cluster = row*nrows + col
		ax = axs[row,col]
		labels,freqs = zip(*sorted(d["unique"][str(cluster)].items(),key=lambda item:item[1],
							reverse=True)[:cutoff])
		ax.plot(freqs,'k--',linewidth=2)
		artist.adjust_spines(ax)
		ax.set_xticks(xrange(len(freqs)))
		ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
		ax.set_title(artist.format('Cluster %d'%cluster))
plt.tight_layout()
plt.savefig('../imgs/frequent-drugs-in-taxonomy-clusters.png')