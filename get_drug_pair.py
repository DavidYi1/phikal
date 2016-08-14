# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:07:42 2016

@author: David
"""

import numpy as np
##Some words like "sound" or "drug" I'm choosing to ignore
ignorewords = [571,626,237]

matrix = np.load("interaction_matrix-2015-11-28-w-deduped-curated-drug-names.npy")
#Most Common and Highest in Most Common
most_common = matrix[0][0]
max_row = 0
max_col = 0
for i in range(len(matrix)):
    if matrix[i][i] > most_common and i not in ignorewords:
        most_common = matrix[i][i]
        max_row = i



print "# of highest occurence" 
print most_common
print "Row #" 
print max_row

max_value = matrix[max_row][0]

for i in range(len(matrix)):
    if matrix[max_row][i] > max_value and i != max_row and i not in ignorewords:
        max_value = matrix[max_row][i]
        max_col = i

print "Col #" 
print max_col
print "Max Value"
print max_value



'''
#Highest Value

value = matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > value and i!=j and i not in ignorewords and j not in ignorewords:
            value = matrix[i][j]
            print i 
            print j
print value
'''
#Percentage based
value = matrix[0][0]
high_percentage = 0
for i in range(len(matrix)):
    if matrix[i][i] != 0:  
        for j in range(len(matrix)):
            if i!=j and matrix[j][j] !=0:
                if i not in ignorewords and j not in ignorewords:
                    
                    if matrix[i][j]/matrix[i][i] > high_percentage or matrix[i][j]/matrix[j][j] > high_percentage:
                        high = matrix[i][j]/matrix[i][i]
                        if matrix[i][j]/matrix[j][j] > high :
                            high = matrix[i][j]/matrix[j][j]
                        high_percentage = high
                        print matrix[i][j]
                        print i
                        print j
                        print high
                
                        value = matrix[i][j]
print value
print high_percentage



