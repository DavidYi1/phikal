import numpy as np 

from collections import Counter
from awesome_print import ap 
TAB = '\t'
#-- Load effect matrix (rows=document,cols=effect)
effect_matrix = np.loadtxt('../data/effect-matrix.tsv',delimiter=TAB)
effects = open('../data/master-class-list').read().splitlines()
#--- Prevalence of effects

effect_prevalence = {drug:sum(effect_matrix[i,:]==1) 
							for i,drug in enumerate(effects)}

ap(sorted(effect_prevalence.items(),key=lambda item:item[1],reverse=True))