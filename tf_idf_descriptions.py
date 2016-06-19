# -*- coding: utf-8 -*-
import json
from gensim import corpora, models, similarities

texts = []
drugs = []
file_names = []
initial_file = json.load(open('db.json','r'))
for x,y in enumerate(initial_file):
    file_names.append(y)


for item in initial_file.itervalues():
    texts.append(item['processed_text'])
    for word in item['drugs']:
        drugs.append(word)

drugs = list(set(drugs))        
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
key = dictionary.token2id

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

for x,y in enumerate(corpus_tfidf):
    initial_file[file_names[x]]['tfidf'] = y
    
json.dump(initial_file,open('db_tfidf.json','w'))
json.dump(key,open('tf_idf_keys.json','w'))
