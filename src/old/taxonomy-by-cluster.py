import json

import utils as tech 
import numpy as np 

from awesome_print import ap 
from collections import Counter

from progress.bar import Bar 

READ = 'rb'
taxonomy = json.load(open('../data/drug-taxonomy.json',READ))
clusters = json.load(open("../data/drugs-in-each-cluster-jaccard.json",READ))
db = json.load(open('../data/db.json',READ))

d = {cluster: dict(Counter(tech.flatten([taxonomy[drug]["effects"] for drug in clusters[cluster]]))) 
							for cluster in clusters}


def getEffects(doc):
	return list(set(tech.flatten(taxonomy[drug]["effects"] for drug in doc["drugs"])))

##Reverse dictionary
classes = list(set((tech.flatten([taxonomy[drug]["effects"] for drug in taxonomy]))))
with open('../data/taxonomy-classes','wb') as fid:
	for effect in classes:
		print>>fid,effect
drugs = open('../data/master-drug-list',READ).read().splitlines()
m = np.loadtxt('../data/occurence-matrix.tsv',delimiter='\t')


reversed_taxonomy = {effect:[drug for drug in taxonomy if effect in taxonomy[drug]["effects"]] 
						for effect in set(classes)}

bar = Bar("Filling taoxonomy matrix",max =(len(classes)*len(classes)-1)/2)
taxonomy_interaction = np.zeros((len(classes),len(classes)))
for i in xrange(len(classes)):
	for j in xrange(i+1):
		taxonomy_interaction[i][j] = len([doc for doc in db if classes[i] in getEffects(db[doc])
															and classes[j] in getEffects(db[doc])])
		bar.next()
bar.finish()

np.savetxt('../data/taxonomy-matrix.tsv',taxonomy_interaction + np.tril(taxonomy_interaction,k=-1).T,fmt='%d',delimiter='\t')