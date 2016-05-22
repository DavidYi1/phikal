import json

from awesome_print import ap 
import numpy as np 


def iqr(data):
	return 0.5* (np.percentile(data,75)-np.percentile(data,25))
tally= json.load(open('../data/drugs-that-actually-occurr.json','rb'))


ap(tally)
ap(np.median(tally.values()))
ap(9287/float(len(tally)))
ap(iqr(tally.values()))