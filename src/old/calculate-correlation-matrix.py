import json 

import numpy as np 
import utils as tech 

from awesome_print import ap 
from progress.bar import Bar 
READ = 'rb'

m = np.loadtxt('../data/occurence-matrix.tsv',delimiter='\t')
x = np.array([[a.dot(b)/float(len(a)) 
			if a.sum()*b.sum()>0 else 0 for a in m] for b in m])

np.savetxt('../data/correlation-matrix.tsv',x,delimiter='\t',fmt='%.04f')