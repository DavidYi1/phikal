import json

import matplotlib.pyplot as plt 
import numpy as np 

READ = 'rb'

def flatten(foo):
    for x in foo:
        if hasattr(x, '__iter__'):
            for y in flatten(x):
                yield y
        else:
            yield x

def matrix_jaccard(m,jacc):
    idx = np.tril_indices_from(jacc)
    for i,j in zip(*idx):
        jacc[i,j] = jaccard(m[i,:],m[j,:])
    jacc += np.tril(jacc,k=-1).T
    return jacc

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

def discrete_cmap(N, base_cmap=None):
    """Create an N-bin discrete colormap from the specified input map"""

    # Note that if base_cmap is a string or None, you can simply do
    #    return plt.cm.get_cmap(base_cmap, N)
    # The following works for string, None, or a colormap instance:

    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

def jaccard(one,two):
    return np.logical_and(one,two).sum()/float(np.logical_or(one,two).sum())

