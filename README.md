# phikal
Computational analysis of hallucinogens



## Preprocessing
1. Assume a folder _forums_ contains each post in a text file. 

## Quickstart 

## Requirements 

jq

     brew install jq

numpy
matplotlib 
nltk

Used codes from "Street Drug Codes" at MacArthur.virginia.edu

TODO: Create setup

1. Go through list of drugs with attention to systematizing plant names

May include: https://en.wikipedia.org/wiki/List_of_psychoactive_plants

If each effect occurs randomly, then the chance of any document having at least
one effect is 1/n where n is the number of effects under study. 

We are interested in the co-occurrence of effects. The chance of two events occurring
randomly is 1/n * 1/n. We, accordingly, exclude any event that occurs fewer than 

(1/n * 1/n * N) + IQR that is any variable within one iqr of the expected occurence
