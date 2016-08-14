# -*- coding: utf-8 -*-

import json
import operator

only_lsd = {}
only_mdma = {}
both_drugs = {}
initial_file = json.load(open('db.json','r'))
for x,y in enumerate(initial_file):
    if "mdma" in initial_file[y]["drugs"] and "lsd" in initial_file[y]["drugs"]:
        for word in initial_file[y]["processed_text"]:
            if word not in both_drugs:
                both_drugs[word] = 1
            else:
                both_drugs[word] = both_drugs[word] + 1
                
    elif "mdma" in initial_file[y]["drugs"]:
        for word in initial_file[y]["processed_text"]:
            if word not in only_mdma:
                only_mdma[word] = 1
            else:
                only_mdma[word] = only_mdma[word] + 1
                
    elif "lsd" in initial_file[y]["drugs"]:
        for word in initial_file[y]["processed_text"]:
            if word not in only_lsd:
                only_lsd[word] = 1
            else:
                only_lsd[word] = only_lsd[word] + 1
for x in range(30):
    with open("only_lsd.txt","a") as fid:
        c = max(only_lsd.iteritems(), key=operator.itemgetter(1))[0]
        fid.write(str(c) + "   " + str(only_lsd[c]) +"\n")
        only_lsd.pop(c)
        
    with open("only_mdma.txt","a") as fid1:
        d = max(only_mdma.iteritems(), key=operator.itemgetter(1))[0]
        fid1.write(str(d) + "   " +  str(only_mdma[d])+"\n")
        only_mdma.pop(d)
        
    with open("both_drugs.txt","a") as fid2:
        q = max(both_drugs.iteritems(), key=operator.itemgetter(1))[0]
        fid2.write(str(q) + "   " + str(both_drugs[q])+"\n")
        both_drugs.pop(q)

