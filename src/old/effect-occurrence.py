import json 

import numpy as np 

from awesome_print import ap 
#create effect matrix

def iqr(data):
	return 0.5*(np.percentile(data,75)-np.percentile(data,25))

db = json.load(open('../data/db.json','rb'))
effects = open('../data/master-effect-list','rb').read().splitlines()
taxonomy = json.load(open('../data/drug-taxonomy.json','rb'))
def process(effect,entry):
	effects = list(set([x for drug in entry["drugs"]
						  for x in taxonomy[drug]["effects"]]))

	#Calling x so as not to shadow the argument EFFECT passed to function
	return 1 if effect in effects else -1

ap('Calculating occurrent matrix')
m = np.array([[process(effect,entry)
					for entry in db.values()]
					for effect in effects],dtype=int)

np.savetxt('../data/effect-matrix.tsv', m, fmt='%d',delimiter='\t')

tally = {effect:sum(m[i,:]==1) for i,effect in enumerate(effects)}

json.dump(tally,open('../data/frequency-of-effects.json','wb'))
json.dump({'expected occurrence':len(db)/float(len(effects)),
		'iqr':iqr(tally.values())},open('../data/thresholds.json','wb'))

#--- Exclude effects that never occurred 

idx = [i for i,effect in enumerate(effects) if tally[effect]>200]
better_m = m[idx,:]

np.savetxt('../data/effect-matrix-actually-occurred.tsv',better_m,
	delimiter='\t', format='%d')

with open('../data/effects-that-actually-occurred','wb') as fid:
	for i in idx:
		print>>fid,effects[i]

#_-Check
ap({effects[i]:sum(better_m[i,:]==1) for i in xrange(better_m.shape[0])})

