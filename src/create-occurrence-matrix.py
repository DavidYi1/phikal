import numpy as np 

import json 

import numpy as np 
import utils as tech 

from awesome_print import ap 
from progress.bar import Bar 
from collections import Counter

READ = 'rb'

drugs = open('../data/drugs-that-actually-occurr',READ).read().splitlines()
db =  json.load(open('../data/db.json',READ))

def process(drug,entry):
	bar.next()
	return	1 if drug in entry['drugs'] else 0

bar = Bar("Filling occurence matrix",max =len(db)*len(drugs))
m = np.array([[process(drug,entry)
					for entry in db.itervalues()]
					for drug in drugs],dtype=int)

bar.finish()

np.savetxt('../data/occurence-matrix.tsv',m, delimiter='\t',fmt='%d')	
print m.shape