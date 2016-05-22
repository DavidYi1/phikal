import json

import utils as tech
import matplotlib.pyplot as plt 
import Graphics as artist 

from awesome_print import ap 
from collections import Counter
from matplotlib import rcParams

rcParams['text.usetex'] = True
READ = 'rb'
db = json.load(open('../data/db.json',READ))
taxonomy = json.load(open('../data/drug-taxonomy.json',READ))
cutoff = 20 #Top n words to show

#How often does each drug occur in the database?
tally = dict(Counter(list(tech.flatten([doc["drugs"] for doc in db.itervalues()]))))
'''
labels,freqs = zip(*sorted(tally.items(),key=lambda item:item[1],reverse=True)[:cutoff])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs,'k--',linewidth=2)
artist.adjust_spines(ax)
ax.set_xticks(xrange(len(labels)))
ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
ax.set_ylabel(artist.format('No. of mentions'))

plt.tight_layout()
plt.savefig('../imgs/overall-drug-frequency.png')

del fig,ax 

#How often does each effect occur in the database?
effect_tally = dict(Counter(list(tech.flatten([taxonomy[drug]["effects"] 
				for drug in tally.keys()]))))

ap(effect_tally)


labels,freqs = zip(*sorted(effect_tally.items(),key=lambda item:item[1],reverse=True)[:cutoff])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs,'k--',linewidth=2)
artist.adjust_spines(ax)
ax.set_xticks(xrange(len(labels)))
ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
ax.set_ylabel(artist.format('No. of mentions'))

plt.tight_layout()
plt.savefig('../imgs/effect-frequency.png')

del fig,ax 
'''
'''
#How often does each class occur in the database?
class_tally = dict(Counter(list(tech.flatten([taxonomy[drug]["class"] 
				for drug in tally.keys()]))))

ap(class_tally)
'''

for drug in taxonomy:
	if 'class' not in taxonomy[drug]:
		ap(drug) 
'''
labels,freqs = zip(*sorted(class_tally.items(),key=lambda item:item[1],reverse=True)[:cutoff])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs,'k--',linewidth=2)
artist.adjust_spines(ax)
ax.set_xticks(xrange(len(labels)))
ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
ax.set_ylabel(artist.format('No. of mentions'))

plt.tight_layout()
plt.savefig('../imgs/class-frequency.png')

del fig,ax 
'''