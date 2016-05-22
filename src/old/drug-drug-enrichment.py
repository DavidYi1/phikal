import numpy as np 
import scipy, itertools
import matplotlib.pyplot as plt 
import Graphics as artist

from matplotlib import rcParams

rcParams['text.usetex'] = True
m = np.loadtxt('../data/drug-matrix-actually-occurred.tsv',delimiter='\t',dtype=int)
m += 1 
m /= 2 
#NumPy's logical functions only work on vectors of 1s and 0s
#It only makes sense to calculate the Jaccard similarity of drugs with data in the corpus.
#It may also be informative to calculate the tf-idf of individual drugs
jacc = np.zeros((m.shape[1],m.shape[1]),dtype=float)

def jaccard(one,two):
	return np.logical_and(one,two).sum()/float(np.logical_or(one,two).sum())

idx = np.tril_indices_from(jacc)
for i,j in zip(*idx):
	jacc[i,j] = jaccard(m[:,i],m[:,j])

jacc += np.tril(jacc,k=-1).T

np.savetxt('../data/drug-jaccard-similarity-actually-occurred.tsv',jacc,delimiter='\t',fmt='%d')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(jacc,interpolation='nearest',aspect='equal',cmap=plt.cm.bone_r,vmin=0,vmax=1)
artist.adjust_spines(ax)
plt.colorbar(cax)
plt.show()
