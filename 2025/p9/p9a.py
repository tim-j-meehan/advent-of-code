import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
import networkx as nx
cnt = 0

def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)
fp = open(sys.argv[1])



first = True 
vals = []
cnt = 0
doit = False
myvals = []
lastline = None
cnt2=0
myvals = []

circ = []
for line in fp.readlines():
#    print(line,len(line))
    vals = [int(x) for x in line.split(',')]
    if vals[0] >= 50278:
        myvals.append(vals)
#    if vals[0] <= 48472:
#        myvals.append(vals)
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
#        if dist < mindist:
#            mindist = dist
#            minii= ii
#            minkk=kk

skeys = sorted(lookup.keys())
a,b = lookup[skeys[-1]]
print("one corner",mymat[a],"other corner",mymat[b])
diff = mymat[a] - mymat[b]
print((diff[0]+1) * (diff[1]+1))



