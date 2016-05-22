import json 

from awesome_print import ap 


clusters = [cluster for cluster in json.load(open('../data/drug-clusters.json','rb')).itervalues()
					if len(cluster) > 1]

ap(clusters)