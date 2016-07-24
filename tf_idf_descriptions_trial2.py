# -*- coding: utf-8 -*-
import json
from gensim import corpora, models, similarities
import random
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer

import numpy as np

texts = []
drugs = []
file_names = []

start_tf_idf_scores = {}
all_tf_idf_scores = []

initial_file = json.load(open('db.json','r'))
for x,y in enumerate(initial_file):
    file_names.append(y)
    start_tf_idf_scores[y] = []

for item in initial_file.itervalues():
    texts.append(item['processed_text'])
    for word in item['drugs']:
        drugs.append(word)

drugs = list(set(drugs))
Num_docs = len(initial_file)
'''
words = []
for text_set in texts:
    for word in text_set:
        words.append(word)
words = list(set(word))

'''
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
key = dictionary.token2id

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

for x,y in enumerate(corpus_tfidf):
    for tfidf_pair in y:
        start_tf_idf_scores[file_names[x]].append(y) 
        #adds initial tf-idf scores to dictionary
        all_tf_idf_scores.append(tfidf_pair[1])
        #adds it to list of all scores\

words_per_doc = []
all_words = []
for doc in texts:
    words_per_doc.append(len(doc))
    for word in doc:
        all_words.append(word) ##all words contains list of all the words used in all the documents
        
total_values_per_iteration = len(set(all_words)) * Num_docs
for i in range(total_values_per_iteration - len(all_tf_idf_scores)):
    all_tf_idf_scores.append(0.0)
    ## all of the unmentioned words
        
'''
json.dump(initial_file,open('db_tfidf.json','w'))
json.dump(key,open('tf_idf_keys.json','w'))
'''

n_iterations = 1000
widgets = ['Something: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval = n_iterations).start()

for x in range(n_iterations):
    new_corpus = []
    for size in words_per_doc:
        x = random.sample(all_words,size)
        new_corpus.append(x)
    
    new_corpus = [dictionary.doc2bow(text) for text in new_corpus]
    new_corpus = [dictionary.doc2bow(text) for text in new_corpus]
    new_tfidf = models.TfidfModel(new_corpus)
    new_corpus_tfidf = new_tfidf[new_corpus]
    
    words_added = 0
    
    for doc in new_corpus_tfidf:
        for x,value in enumerate(doc): 
            all_tf_idf_scores.append(value[1])
            words_added += 1
    while words_added < (total_values_per_iteration):
        all_tf_idf_scores.append(0.0) ##inflate with 0's of the other words
        words_added += 1
    pbar.update(x)#progress bar
    
pbar.finish()

with open("all_tf_idf_score.txt" ,"w") as fid:
    for value in all_tf_idf_scores:
        fid.write(value + '\n')

json.dump(start_tf_idf_scores,open('start_values.json','w'))
    
        



