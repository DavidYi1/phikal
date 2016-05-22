import json 

import numpy as np 
import utils as tech 

from awesome_print import ap 
from progress.bar import Bar 
READ = 'rb'

drugs = open('master-drug-list',READ).read().splitlines()
db =  json.load(open('db.json',READ))

m = np.zeros((len(drugs),len(drugs)),dtype=int)
idx = np.tril_indices_from(m)

bar = Bar("Filling comention matrix",max = len(idx[0]))
for i,j in zip(*idx):
	m[i][j] = len([entry for entry in db.itervalues() if 
				drugs[i] in entry['drugs'] and drugs[j] in entry['drugs']])

	bar.next()
bar.finish()

np.savetxt('comention-matrix.tsv',m+np.triu(m.T,k=1), delimiter='\t',fmt='%d')	