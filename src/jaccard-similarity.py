import numpy as np 
import utils as tech 
import matplotlib.pyplot as plt 
import Graphics as artist 

from matplotlib import rcParams
from progress.bar import Bar 

rcParams['text.usetex'] = True
'''
m = np.loadtxt('../data/occurence-matrix.tsv',delimiter='\t')
print m.shape

jacc = np.zeros((m.shape[0],m.shape[0]),dtype=float)

idx = np.tril_indices_from(jacc)
bar = Bar("Filling jaccard matrix",max =len(idx[0]))
for i,j in zip(*idx):
	jacc[i,j] = tech.jaccard(m[i,:],m[j,:])
	bar.next()
bar.finish()
jacc += np.tril(jacc,k=-1).T

np.savetxt('../data/drug-jaccard-similarity-actually-occurred.tsv',jacc,delimiter='\t',fmt='%04f')

print jacc.sum(axis=0)
'''
#m = np.loadtxt('../data/drug-jaccard-similarity-actually-occurred.tsv',delimiter='\t')

'''
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.hist(np.tril(m,k=-1).ravel())
cax = ax.imshow(m,interpolation='nearest',aspect='equal',cmap=plt.cm.bone_r)
artist.adjust_spines(ax)
plt.colorbar(cax)
plt.tight_layout()
plt.show()
'''
