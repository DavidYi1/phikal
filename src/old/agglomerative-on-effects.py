import itertools, brewer2mpl

import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist
import matplotlib.ticker as plticker


from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering 
from matplotlib import rcParams
from awesome_print import ap 
rcParams['text.usetex'] = True 

m = np.loadtxt('../data/effect-matrix.tsv',delimiter='\t')
effects = open('../data/master-class-list','rb').read().splitlines()

params = {"n_components":4,"covariance_type":"spherical"}

xm = m.dot(m.T)
xm /= m.shape[1]



pca = PCA(n_components=8,whiten=True)
X = pca.fit_transform(xm)
print pca.explained_variance_ratio_
nclus = 3

clustering = AgglomerativeClustering(linkage='ward', n_clusters=nclus)
Y = clustering.fit_predict(X)

d = {label:[effect for i,effect in enumerate(effects)
                    if clustering.labels_[i] == label] 
                for label in np.unique(clustering.labels_)}

ap(d)
ct = [sum(m[:,i]>0) for i in xrange(m.shape[0])]
ap(dict(zip(effects,ct)))
'''
colors = dict(zip(np.unique(clustering.labels_),
            brewer2mpl.get_map('Set2', 'qualitative',8).mpl_colors))

shapes = dict(zip(np.unique(clustering.labels_),['o','s','*','x','D']))
loc = plticker.MultipleLocator(base=1.0) # this locator puts ticks at regular intervals

fig, axs = plt.subplots(ncols=2,sharex=True,sharey=True,figsize=(8,8))

axs[0].scatter(X[:,0],X[:,1],c=X[:,2],cmap=plt.cm.seismic,s=35, clip_on=False)
artist.adjust_spines(axs[0])
axs[0].set_xlabel(artist.format("PC 1"))
axs[0].set_ylabel(artist.format("PC 2"))
axs[0].set_aspect('equal')
axs[0].xaxis.set_major_locator(loc)
for i in xrange(X.shape[0]):
    axs[1].plot(X[i,0],X[i,1],c=colors[Y[i]],marker=shapes[Y[i]],
        markersize=8,alpha=0.6, clip_on=False)
artist.adjust_spines(axs[1])
axs[1].set_aspect('equal')
axs[1].set_xlabel(artist.format("PC 1"))
axs[1].set_ylabel(artist.format("PC 2"))
plt.tight_layout()
plt.savefig('../imgs/effect-matrix-w-agglomerative-clusters.png')
'''