
import json
import operator
import matplotlib.pyplot as plt

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer
    

only_lsd = {}
only_mdma = {}
both_drugs = {}
either_drugs = {}

highest_only_lsd = {}
highest_only_mdma = {}
highest_both_drugs = {}
i = 0
initial_file = json.load(open('db.json','r'))
for x,y in enumerate(initial_file):
    
    if "mdma" in initial_file[y]["drugs"] or "lsd" in initial_file[y]["drugs"]:
        i = i + 1
        for word in initial_file[y]["processed_text"]:
            if word not in either_drugs:
                either_drugs[word] = 1
            else:
                either_drugs[word] = either_drugs[word] + 1
    if "mdma" in initial_file[y]["drugs"] and "lsd" in initial_file[y]["drugs"]:
        for word in initial_file[y]["processed_text"]:
            if word not in both_drugs:
                both_drugs[word] = 1
            else:
                both_drugs[word] = both_drugs[word] + 1
        
    if "lsd" in initial_file[y]["drugs"]:
        for word in initial_file[y]["processed_text"]:
            if word not in only_lsd:
                only_lsd[word] = 1
            else:
                only_lsd[word] = only_lsd[word] + 1
                
    if "mdma" in initial_file[y]["drugs"]:
        for word in initial_file[y]["processed_text"]:
            if word not in only_mdma:
                only_mdma[word] = 1
            else:
                only_mdma[word] = only_mdma[word] + 1

widgets = ['Something: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
           
pbar = ProgressBar(widgets=widgets, maxval = i).start()

print i

a = 0
for word in either_drugs:
    if word in only_mdma and word in only_lsd and word not in both_drugs:
        both_drugs[word] = (only_mdma[word] + only_lsd[word])/2 #Taking Average
        only_lsd.pop(word)
        only_mdma.pop(word)        
    if word in both_drugs and word in only_lsd:
        only_lsd.pop(word)
    if word in both_drugs and word in only_mdma:
        only_mdma.pop(word)
    #a = a + 1
    pbar.update(a)
    
pbar.finish()


for x in range(10):
    c = max(only_lsd.iteritems(), key=operator.itemgetter(1))[0]
    highest_only_lsd[c] = only_lsd[c]
    only_lsd.pop(c)
        
    d = max(only_mdma.iteritems(), key=operator.itemgetter(1))[0]
    highest_only_mdma[d] = only_mdma[d]
    only_mdma.pop(d)
    
    q = max(both_drugs.iteritems(), key=operator.itemgetter(1))[0]
    highest_both_drugs[q] = both_drugs[q]
    both_drugs.pop(q)

print highest_only_lsd

plt.bar(range(len(highest_only_lsd)), highest_only_lsd.values(), align='center')
plt.xticks(range(len(highest_only_lsd)), highest_only_lsd.keys())
plt.savefig('only_lsd.png')

plt.show()


