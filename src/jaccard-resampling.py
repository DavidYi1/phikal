import numpy as np 
import zipfile
from progress.bar import Bar

'''
m = np.loadtxt('../data/occurence-matrix.tsv',delimiter='\t')

#What is a significant Jaccard similarity?
n = 10000

bar = Bar("Resampling jaccard matrix",max =n)
for rep in xrange(n):
	n = m.copy()
	np.random.shuffle(n)


	with open('../data/resampling/jaccard-similarities','a+') as fid:
		values = np.tril(tech.matrix_jaccard(n,np.zeros((m.shape[0],m.shape[0]))),k=-1).ravel()
		for value in values:
			print>>fid,value
	bar.next()
bar.finish()
'''

data = np.loadtxt('../data/resampling/jaccard-similarities',delimiter='\n')
cutoff = 5/float(161*80)
print 1-cutoff
print np.percentile(data,1-cutoff)  
#.030888030888 Before bonferroni
#0.206349206349 after