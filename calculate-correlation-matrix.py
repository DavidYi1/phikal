import json 

import numpy as np 
import utils as tech 

from awesome_print import ap 
from progress.bar import Bar 
READ = 'rb'

drugs = open('master-drug-list',READ).read().splitlines()
db =  json.load(open('db.json',READ))

def process(drug,entry):
	bar.next()
	return	1 if drug in entry['drugs'] else -1 

bar = Bar("Filling occurence matrix",max =len(db)*len(drugs))
m = np.array([[process(drug,entry)
					for entry in db.itervalues()]
					for drug in drugs],dtype=int)

bar.finish()

np.savetxt('occurence-matrix.tsv',m, delimiter='\t',fmt='%d')	

x = np.array([[a.dot(b)/float(len(a)) 
			if a.sum()*b.sum()>0 else 0 for a in m] for b in m])

np.savetxt('correlation-matrix.tsv',x,
			delimiter='\t',fmt='%.04f')