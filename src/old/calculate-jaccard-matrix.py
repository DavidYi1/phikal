import json 

import numpy as np 
import utils as tech 

from sklearn.metrics import jaccard_similarity_score
from progress.bar import Bar 
READ = 'rb'

data = np.loadtxt('../data/occurence-matrix.tsv',delimiter='\t')	

n_drugs,n_docs = data.shape

def jaccard(one,two):
	a = ((one==1) * (two==1)).sum()
	b = ((one==1) * (two==-1)).sum()
	c = ((one==-1) * (two==1)).sum()

	return a/float(a+b+c) if a > 0 else 0

bar = Bar("Filling jaccard similarity matrix",max =n_drugs*(n_drugs-1)/2)
x = np.zeros((n_drugs,n_drugs))
for i in xrange(n_drugs):
	for j in xrange(i):
		x[i,j] = jaccard(data[i,:],data[j,:])
		bar.next()
bar.finish()


x += np.tril(x,k=-1).T
np.savetxt('../data/jaccard-matrix.tsv',x,
			delimiter='\t',fmt='%.04f')
