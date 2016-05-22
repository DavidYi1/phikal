import json 

import numpy as np 
import utils as tech

from awesome_print import ap 
from collections import Counter

db = json.load(open('../data/db.json','rb'))
drugs = open('../data/list_of_drugs','rb').read().splitlines()

#----- Descriptive Statistics
frac = len([x for x in db if len(db[x]["drugs"])>0])/float(len(db))
ap("Fraction of db with recognized drugs: %.04f"%frac)

tally = dict(Counter(tech.flatten([db[entry]["drugs"] for entry in db])))
drugs_that_occur = {drug:tally[drug] if drug in tally else 0 for drug in drugs}

dto = drugs_that_occur.values()
with open('../data/drugs-that-actually-occurr','wb') as fid:
	for drug in tally:
		print>>fid,drug

json.dump(tally,open('../data/drugs-that-actually-occurr.json','wb'))

#--- What entries have no drugs?
'''
for entry in db:
	if len(db[entry]["drugs"]) == 0:
		ap(db[entry]["processed_text"])
'''
#-----------------------------------

m = np.array([[1 if drug in db[entry]["drugs"] else -1 
						for drug in tally] 
						for entry in db], dtype=int)

del drugs
drugs = open('../data/drugs-that-actually-occurr','rb').read().splitlines()
idx = [i for i,drug in enumerate(drugs) if tally[drug]>0]
better_m = m[:,idx]
with open('../data/drugs-that-occurred enough','wb') as fid:
	for i in idx:
		print>>fid,drugs[i]

np.savetxt('../data/drug-matrix-actually-occurred.tsv',better_m,
	delimiter='\t', fmt='%d')
