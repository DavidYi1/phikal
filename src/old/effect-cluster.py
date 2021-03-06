import json, brewer2mpl

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist
import matplotlib.ticker as plticker

#import seaborn as sns

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from awesome_print import ap 
from matplotlib import rcParams
rcParams['text.usetex'] = True

m = np.loadtxt('../data/effect-matrix-actually-occurred.tsv',delimiter='\t')
effects = open('../data/effects-that-actually-occurred','rb').read().splitlines()
x = m.dot(m.T)
x /= float(m.shape[1])
#var = x.var(axis=0)
#mu = x.mean(axis=0)
#x = (x - mu)/var

'''
#Visualize correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
sns.heatmap(x,ax=ax,cmap='seismic', square=True, vmin=-1,vmax=1)
ax.set_yticklabels(effects,rotation='horizontal')
ax.set_xticklabels(effects[::-1],rotation='vertical')
plt.tight_layout()
plt.savefig('../imgs/effect-correlation-matrix.png')
del fig,ax
'''
pca = PCA(n_components=10)
X = pca.fit_transform(x)

#Scree plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(1+np.arange(5),pca.explained_variance_ratio_[:5],0.35,
	color='k', align='center',alpha=0.6)
ax.plot(1+np.arange(5),np.cumsum(pca.explained_variance_ratio_[:5]),
		'k.--',linewidth=2,markersize=15)
artist.adjust_spines(ax)
ax.set_ylabel(artist.format('Explained Variance'))
ax.set_xlabel(artist.format('Principal Component'))
ax.set_xlim(xmin=0.5,xmax=5.5)
plt.tight_layout()
plt.savefig('../imgs/scree-plot.png')
del fig,ax

'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X[:,0],X[:,1],c=X[:,2],cmap=plt.cm.seismic,clip_on=False)
artist.adjust_spines(ax)
ax.set_xlabel(artist.format('PC 1'))
ax.set_ylabel(artist.format('PC 2'))
ax.set_aspect('equal')
loc = plticker.MultipleLocator(base=10.0)
ax.xaxis.set_major_locator(loc)
ax.yaxis.set_major_locator(loc)
plt.tight_layout()
plt.show()
'''


#Kmeans just as good as agglomerative here 
silhouettes = {}
to_save = {}
for nclus in xrange(2,6):
	kmeans = KMeans(n_clusters=nclus,n_init=2)
	labels = kmeans.fit_predict(X)

	clustering = AgglomerativeClustering(linkage='average', n_clusters=nclus)
	Y = clustering.fit_predict(X)

	silhouettes[nclus]=silhouette_score(X,labels)
	to_save[nclus] = {"silhouette_score":silhouettes[nclus],
					  "labels":labels.tolist()}
	print '%d clusters: %.04f'%(nclus,silhouettes[nclus])

json.dump(to_save,open('../data/effect-matrix-kmeans-cluster-labels.json','wb'))

fig = plt.figure()
ax = fig.add_subplot(111)

clusters,scores = zip(*sorted(silhouettes.items(),
				key=lambda item: item[0],reverse=True))

ax.plot(clusters, scores,'k.--',linewidth=2,markersize=20)
artist.adjust_spines(ax)
ax.set_xticks(clusters)
ax.set_xlim(xmin=min(clusters)-1,xmax=max(clusters)+1)
ax.set_xlabel(artist.format('No. of clusters'))
ax.set_xticklabels(map(artist.format,clusters))

ax.set_ylabel(artist.format('Silhouette score'))
ax.set_yticks([0.6,0.8,1])
plt.tight_layout()
plt.savefig('../imgs/effect-silhouette-score.png')
del fig,ax

labels = to_save[2]["labels"]
colors = {label:color for label,color in zip(np.unique(labels),
						brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors)}
shapes = {label:shape for label,shape in zip(np.unique(labels),
									['o','s','*','x','D'])}

fig,axs = plt.subplots(ncols=2,sharex=True,sharey=True)
#display pcs on left
axs[0].scatter(X[:,0],X[:,1],c=X[:,2],
	cmap=plt.cm.seismic,alpha=0.8, clip_on=False)
artist.adjust_spines(axs[0])
axs[0].set_xlabel(artist.format('PC 1'))
axs[0].set_ylabel(artist.format('PC 2'))
axs[0].set_aspect('equal')
loc = plticker.MultipleLocator(base=1.0)
axs[0].xaxis.set_major_locator(loc)
axs[0].yaxis.set_major_locator(loc)

#--Print out effects in each cluster
d = {cluster:[effect for i,effect in enumerate(effects)
					if labels[i]==cluster] for cluster in np.unique(labels)}

for i in xrange(X.shape[0]):
	axs[1].scatter(X[i,0],X[i,1],marker=shapes[labels[i]],c=colors[labels[i]],alpha=0.8)
artist.adjust_spines(axs[1])
axs[1].set_xlabel(artist.format('PC 1'))
axs[1].set_ylabel(artist.format('PC 2'))
axs[1].annotate('\n'.join(d[1]),xy=(0.05,0.6),color=colors[1],xycoords='axes fraction')
axs[1].annotate('\n'.join(d[0]),xy=(0.5,0.06),color=colors[0],xycoords='axes fraction')

plt.tight_layout()
plt.savefig('../imgs/effect-matrix-pca-w-clusters.png')

