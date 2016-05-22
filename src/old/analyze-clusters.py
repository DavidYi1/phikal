import json

from sys import argv
from awesome_print import ap 

filename = argv[1]


labels = json.load(open('../data/%s-matrix-kmeans-cluster-labels.json'%filename,'rb'))["4"]["labels"]

if filename != 'taxonomy':
	drugs = open('../data/master-drug-list','rb').read().splitlines()
	clusters = {label:[drug for i,drug in enumerate(drugs)
			if labels[i]==label] for label in set(labels)}

else: 
	effects = open('../data/taxonomy-classes','rb').read().splitlines()
	clusters={label:[effect for i,effect in enumerate(effects) 
						if labels[i]==label] for label in set(labels)}

json.dump(clusters, open("../data/drugs-in-each-cluster-%s.json"%filename,'wb'))
ap(clusters)
