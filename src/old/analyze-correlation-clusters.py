import json

from awesome_print import ap 
drugs = open('master-drug-list').read().splitlines()
labels = json.load(open('correlation-matrix-kmeans-cluster-labels.json','rb'))["2"]["labels"]


clusters = {label:[drug for i,drug in enumerate(drugs)
			if labels[i]==label] for label in set(labels)}

json.dump(clusters, open("drugs-in-each-cluster.json",'wb'))

ap(clusters)
