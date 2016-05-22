import json 

import numpy as np 

from awesome_print import ap 

#threshold = .030888030888
#threshold /= (161*80) #Bonferroni correction
threshold =0.206349206349
ap(threshold)
READ = 'rb'
m = np.loadtxt('../data/drug-jaccard-similarity-actually-occurred.tsv',delimiter='\t')
drugs = open('../data/drugs-that-actually-occurr',READ).read().splitlines()
taxonomy = json.load(open('../data/drug-taxonomy.json',READ))


d = {'%s-%s'%(drugs[i],drugs[j]):m[i,j] 
		for i,j in zip(*np.where(np.tril(m,k=-1)>threshold))}

ap(d)
ap(len(d))
json.dump(d,open('../data/significantly-similar-pairs','wb'))
#Which mixing probabilities occur more than by chance?

#Prevalence of different classes
