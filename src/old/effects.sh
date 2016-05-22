#!/bin/bash
#Create effect by document matrix; Remove effects that never occur in corpus

python effect-occurence.py

#--- Create effect-effect correlation matrix
#--- PCA
#--- Cluster

python effect-cluster.py