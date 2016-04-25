import json

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from matplotlib import rcParams
rcParams['text.usetex'] = True

data = np.loadtxt('correlation-matrix.tsv',delimiter='\t')
pca = PCA(n_components=10)
X = pca.fit_transform(data)

silhouettes = {}
to_save = {}
for nclus in xrange(2,6):
	kmeans = KMeans(n_clusters=nclus,n_init=20)
	kmeans.fit(X)
	labels = kmeans.predict(X)

	silhouettes[nclus]=silhouette_score(X,labels)
	to_save[nclus] = {"silhouette_score":silhouettes[nclus],
					  "labels":labels.tolist()}
	print '%d clusters: %.04f'%(nclus,silhouettes[nclus])

json.dump(to_save,open('correlation-matrix-kmeans-cluster-labels.json','wb'))
fig = plt.figure()
ax = fig.add_subplot(111)

clusters,scores = zip(*sorted(silhouettes.items(),
				key=lambda item: item[1],reverse=True))

ax.plot(clusters, scores,'k.--',linewidth=2,markersize=20)
artist.adjust_spines(ax)
ax.set_xticks(clusters)
ax.set_xlim(xmin=min(clusters)-1,xmax=max(clusters)+1)
ax.set_xlabel(artist.format('No. of clusters'))
ax.set_xticklabels(map(artist.format,clusters))

ax.set_ylabel(artist.format('Silhouette score'))
ax.set_ylim(ymin=0.6,ymax=1)
ax.set_yticks([0.6,0.8,1])
plt.tight_layout()
plt.savefig('silhouette-score.png')