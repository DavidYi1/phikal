
import json
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer
    

only_lsd = {}
only_mdma = {}
both_drugs = {}

i = 0
initial_file = json.load(open('db.json','r'))
for x,y in enumerate(initial_file):
    if "mdma" in initial_file[y]["drugs"] and "lsd" in initial_file[y]["drugs"]:
        i = i + 1
        for word in initial_file[y]["processed_text"]:
            if word not in both_drugs:
                both_drugs[word] = {"frequency": 1, "doc_num" : 0}
            else:
                both_drugs[word]["frequency"] = both_drugs[word]["frequency"] + 1
    elif "lsd" in initial_file[y]["drugs"]:
        i = i + 1
        for word in initial_file[y]["processed_text"]:
            if word not in only_lsd:
                only_lsd[word] = {"frequency": 1, "doc_num" : 0}
            else:
                only_lsd[word]["frequency"] = only_lsd[word]["frequency"] + 1
    elif "mdma" in initial_file[y]["drugs"]:
        i = i + 1
        for word in initial_file[y]["processed_text"]:
            if word not in only_mdma:
                only_mdma[word] = {"frequency": 1, "doc_num" : 0}
            else:
                only_mdma[word]["frequency"] = only_mdma[word]["frequency"] + 1

widgets = ['Something: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval = i).start()
a = 0
b = 0
c = 0
for x,y in enumerate(initial_file):
    if "mdma" in initial_file[y]["drugs"] and "lsd" in initial_file[y]["drugs"]:
        a = a + 1
        for word in both_drugs:
            if word in initial_file[y]["processed_text"]:
                both_drugs[word]["doc_num"] = both_drugs[word]["doc_num"] + 1
    elif "lsd" in initial_file[y]["drugs"]:
        b = b + 1
        for word in only_lsd:
            if word in initial_file[y]["processed_text"]:
                only_lsd[word]["doc_num"] = only_lsd[word]["doc_num"] + 1
    elif "mdma" in initial_file[y]["drugs"]:
        c = c + 1
        for word in only_mdma:
            if word in initial_file[y]["processed_text"]:
                only_mdma[word]["doc_num"] = only_mdma[word]["doc_num"] + 1                     
        pbar.update(a+b+c)
        
pbar.finish()

print both_drugs


print a
print b
print c

with open('LSD_and_MDMA.json', 'w') as outfile:
    json.dump(both_drugs, outfile)
    
with open('LSD_data.json', 'w') as outfile1:
    json.dump(only_lsd, outfile1)
    
with open('MDMA_data.json', 'w') as outfile2:
    json.dump(only_mdma, outfile2)
