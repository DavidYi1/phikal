import json 

import numpy as np
from progress.bar import Bar 


READ = 'rb'
db = json.load(open('../data/db.json','rb'))
taxonomy = json.load(open('../data/drug-taxonomy.json','rb'))
FX = open('../data/effects-that-actually-occurred',READ).read().splitlines()
drugs = open('../data/drugs-that-actually-occurr',READ).read().splitlines()

m = np.zeros((len(drugs),len(FX)))

bar = Bar("Filling occurence matrix",max =m.size)
for i,drug in enumerate(drugs):
	for j,effect in enumerate(FX):
		m[i][j] = sum([1 if (drug in db[entry]["drugs"] and effect in taxonomy[drug]["effects"]) else 0
							for entry in db])
		bar.next()
bar.finish()

np.savetxt('../data/drug-effect-matrix.tsv',m,delimiter='\t',fmt='%d')