import json

import numpy as np 

from awesome_print import ap 
from sys import argv

nclus = argv[1]
labels = json.load(open('../data/effect-correlation-matrix-kmeans-cluster-labels.json','rb'))[str(nclus)]["labels"]
#Only care about labels for two cluster case

effects = open('../data/master-class-list','rb').read().splitlines()
print len(effects)
print len(labels)
d = {cluster:[effect for i,effect in enumerate(effects) if labels[i]==int(cluster)] 
		for cluster in np.unique(labels)}
ap(d)