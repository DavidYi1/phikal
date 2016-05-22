import json, brewer2mpl

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist
import utils as tech 

from collections import Counter
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from matplotlib import rcParams
from sys import argv

filename = argv[1]
nclus = argv[2]
rcParams['text.usetex'] = True
drugs = open('../data/master-drug-list').read().splitlines()
labels = json.load(open('../data/%s-matrix-kmeans-cluster-labels.json'%filename,'rb'))
data = np.loadtxt('../data/%s-matrix.tsv'%filename,delimiter='\t')
pca = PCA(n_components=10)
X = pca.fit_transform(data)

drug_pairs = zip(drugs,drugs)
fig,axs = plt.subplots(ncols=2,sharex=True,sharey=True)
#display pcs on left
axs[0].scatter(X[:,0],X[:,1],c=X[:,2],cmap=plt.cm.seismic,alpha=0.8)
artist.adjust_spines(axs[0])
axs[0].set_xlabel(artist.format('PC 1'))
axs[0].set_ylabel(artist.format('PC 2'))
#overlay clustering on right

if filename != 'taxonomy' and filename != 'effect-correlation':
	colors = ['k' if label == 1 else 'w' for label in labels[nclus]["labels"]]
	shapes = ['o' if color == 'k' else 's' for color in colors]

else:
	color = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors
	shape = ['o','s','*','x','D']
	colors = [color[label] for label in labels[nclus]["labels"]]
	shapes = [shape[label%len(shape)] for label in labels[nclus]["labels"]]
print Counter(colors)
for x,y,c,s in zip(X[:,0],X[:,1],colors,shapes):
	axs[1].scatter(x,y,marker=s,c=c,alpha=0.8)
artist.adjust_spines(axs[1])
axs[1].set_xlabel(artist.format('PC 1'))
axs[1].set_ylabel(artist.format('PC 2'))
plt.tight_layout()
plt.savefig('../imgs/%s-matrix-w-clusters.png'%filename)