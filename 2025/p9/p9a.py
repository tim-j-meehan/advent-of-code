import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
import networkx as nx

fp = open(sys.argv[1])

vals = []
myvals = []

for line in fp.readlines():
    vals = [int(x) for x in line.split(',')]
    if vals[0] >= 50278:
        myvals.append(vals)
mymat = np.array(myvals)
pprint.pprint(mymat)
N = mymat.shape[0]
lookup = {}
mindist = 99999900009
for ii in range(N):
    for kk in range(ii+1,N):
        dif = mymat[ii] - mymat[kk]
        area = dif[0] * dif[1]
        lookup[area] = (ii,kk) 

skeys = sorted(lookup.keys())
a,b = lookup[skeys[-1]]
print("one corner",mymat[a],"other corner",mymat[b])
diff = mymat[a] - mymat[b]
print((diff[0]+1) * (diff[1]+1))
