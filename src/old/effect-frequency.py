import json 

import Graphics as artist
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['text.usetex'] = True

effects = json.load(open('../data/frequency-of-effects.json','rb'))

cuotff=20

labels,freqs = zip(*sorted(effects.items(),key=lambda item: item[1],reverse=True)[:cuotff])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(freqs,'k--',linewidth=2)
artist.adjust_spines(ax)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(map(artist.format,labels),rotation='vertical')
ax.set_ylabel(artist.format('No. of mentions'))
plt.tight_layout()
plt.savefig('../imgs/effect-frequency.png')