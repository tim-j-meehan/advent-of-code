import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../")
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
#        if dist < mindist:
#            mindist = dist
#            minii= ii
#            minkk=kk

skeys = sorted(lookup.keys())
a,b = lookup[skeys[-1]]
print(mymat[a],mymat[b])
diff = mymat[a] - mymat[b]
print((diff[0]+1) * (diff[1]+1))
import pdb
pdb.set_trace()

sets = [set(),]
sets[0].add(lookup[skeys[0]][0])
sets[0].add(lookup[skeys[0]][1])


G=nx.Graph()
for ii in range(N):
    G.add_node(ii)

print(sets)
#for ii in range(1,10):
for ii in range(1,1000):
    a,b = lookup[skeys[ii]]
    G.add_edge(a,b)
    print("adding",a,b)
    if G.is_connected():
        break
        import pdb
        pdb.set_trace()



lens = []
for stuff in nx.connected_components(G):
    lens.append(len(stuff))
print(lens)
lens.sort()
print(lens[-3:])
print("prod is",np.prod(lens[-3:]))


print(G)
   
if False:    
    matcha = False
    matchb = False
    for group in sets:
        if a in group:
            group.add(b)
            matcha = True
            groupa = group
    if match:
        for group in sets:
            if a in group:
                groupa.update(group)
                group = set()
           
    if not match:
        sets.append(set((a,b))) 
pprint.pprint(sets)

print(mindist)
print(minii,mymat[minii])
print(minkk,mymat[minkk])



