import json
import numpy as np 
import matplotlib.pyplot as plt 
import Graphics as artist
import matplotlib.ticker as plticker

from awesome_print import ap 
from matplotlib import rcParams

rcParams['text.usetex'] = True
READ = 'r' 

drugs = open('../data/drugs-that-actually-occurr',READ).read().splitlines()
m = np.loadtxt('../data/occurence-matrix.tsv',delimiter='\t').astype(int)

d = dict(zip(drugs,m.sum(axis=1)))
cutoff = 20

labels,freqs = zip(*sorted(d.items(),key=lambda item:item[1],reverse=True)[:cutoff])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs,'k--',linewidth=2)
artist.adjust_spines(ax)
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
ax.set_ylabel(artist.format('No. of mentions'))
loc = plticker.MultipleLocator(base=1000.0) # this locator puts ticks at regular intervals
ax.yaxis.set_major_locator(loc)

left, bottom, width, height = [0.65, 0.6, 0.3, 0.35]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.hist(d.values(),color='k')
artist.adjust_spines(ax2)

ax2.xaxis.set_major_locator(plticker.MultipleLocator(base=1000.0))
ax2.yaxis.set_major_locator(plticker.MultipleLocator(base=50.0))
for tick in ax2.get_xticklabels():
    tick.set_rotation('vertical')
ax2.set_xlabel(artist.format('No. of mentions'))
ax2.set_ylabel(artist.format('Frequency'))
ax2.axvline(x=freqs[-1],c='r',linewidth=2)


plt.tight_layout()
plt.savefig('../imgs/overall-drug-frequency.png')
