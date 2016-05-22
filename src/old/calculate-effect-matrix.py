import json 

import numpy as np 

from progress.bar import Bar 
from awesome_print import ap 
#create effect matrix

db = json.load(open('../data/db.json','rb'))
effects = open('../data/master-class-list','rb').read().splitlines()
taxonomy = json.load(open('../data/drug-taxonomy.json','rb'))
def process(effect,entry):
	bar.next()

	ap('Looking for whether %s in'%effect)
	ap([effect for drug in entry["drugs"] 
		 		 for effect in taxonomy[drug]["effects"]])
	ap(1 if effect in [effect for drug in entry["drugs"] 
		 		 for effect in taxonomy[drug]["effects"]] else -1 )
	return	1 if effect in [effect for drug in entry["drugs"] 
		 		 for effect in taxonomy[drug]["effects"]] else -1 


bar = Bar("Filling occurence matrix",max =len(db)*len(effects))
m = np.array([[process(effect,entry)
					for entry in db.itervalues()]
					for effect in effects],dtype=int)

bar.finish()
np.savetxt('../data/effect-matrix.tsv', m, fmt='%d',delimiter='\t')
np.savetxt('../data/effect-correlation-matrix.tsv', m.dot(m.T), fmt='%d',delimiter='\t')
