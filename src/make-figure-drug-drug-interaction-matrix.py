import json

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import utils as tech

from scipy.spatial import distance
from scipy.cluster import hierarchy
from awesome_print import ap 
from collections import Counter

READ = 'rb'

drugs = open('../data/drugs-that-actually-occurr',READ).read().splitlines()
m = np.loadtxt('../data/drug-jaccard-similarity-actually-occurred.tsv',delimiter='\t').astype(float)
taxonomy = json.load(open('../data/drug-taxonomy.json',READ))

unique_drug_classes = Counter(tech.flatten([taxonomy[drug]["effects"] 
								for drug in taxonomy if drug in drugs]))

#Give the 10 most common a color
cutoff = 30

palette = sns.color_palette("Set2",cutoff)
colors = {effect:palette[i] for i,effect in 
						enumerate(sorted(dict(unique_drug_classes.iteritems()),
								key=lambda item:item[1],reverse=True)[:cutoff])}

L = hierarchy.linkage(m, method='average')
Z = hierarchy.dendrogram(L,no_plot=True)

cluster_idx = hierarchy.fcluster(L,1.4,depth=4)

drug_clusters = {str(i):[drugs[j] for j,pos in enumerate(cluster_idx) if pos==i] 
				for i in set(cluster_idx)}

ap(drug_clusters)
json.dump(drug_clusters,open('../data/drug-clusters.json','wb'))
row_colors = [colors[taxonomy[drugs[idx]]["effects"][0]] for idx in Z["leaves"]]

cg = sns.clustermap(m,row_linkage=L,col_linkage=L,cmap=plt.cm.Reds,yticklabels=False,
	figsize=(8,8),xticklabels=False)

cg.savefig('../imgs/drug-drug-correlation-w-cluster.png')

'''
ind = hierarchy.fcluster(L, 0.5*d.max(), 'distance')

fig = plt.figure()

ax2 = fig.add_axes([0.09,0.1,0.5,0.6],frame_on=False)
Z1 = hierarchy.dendrogram(L, orientation='left')
ax2.set_xticks([])
ax2.set_yticks([])

ax1 = fig.add_axes([0.3,0.71,0.6,0.2], frame_on=False)
Z2 = hierarchy.dendrogram(L,truncate_mode='lastp',p=5)
ax1.set_xticks([])
ax1.set_yticks([])

axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z1['leaves']
m = m[idx1,:]
m = m[:,idx2]
im = axmatrix.matshow(m, aspect='auto', origin='lower', cmap=plt.cm.bone_r)
axmatrix.set_xticks([])
axmatrix.set_yticks([])
#plt.tight_layout()
'''
plt.show()