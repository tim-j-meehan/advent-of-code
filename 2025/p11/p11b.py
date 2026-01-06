import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib
import copy
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from functools import lru_cache
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
mincnts = []

G=nx.DiGraph()
#for ii in range(N):
#    G.add_node(ii)
    

ncnt = {}
for line in fp.readlines():
    print(line,len(line))
    vals = line.split()
    n_1 = vals[0][:-1]
    ncnt[n_1] = 0
    for n_x in vals[1:]:
        G.add_edge(n_1,n_x)
        ncnt[n_x] = 0
       # G.add_edge(n_x,n_1)

cnt1=0
cnt2=0
cnt3=0


ncnt["out"] = 1
@lru_cache
def find_num_paths(G,stt,stp):
    if stt == stp:
        return 1
    return sum(
        [find_num_paths(G,stt,ni) for ni,no in G.in_edges(stp)]
    )
        

print(find_num_paths(G,'svr','out'))

a=find_num_paths(G,'svr','fft')
b=find_num_paths(G,'fft','dac')
c=find_num_paths(G,'dac','out')

e=find_num_paths(G,'svr','dac')
f=find_num_paths(G,'dac','fft')
g=find_num_paths(G,'fft','out')

print("final",a*b*c+e*f*g)
import pdb
pdb.set_trace()

if True:
    #for pth in nx.all_simple_paths(G,"dac","out"):
#    for pth in nx.all_simple_paths(G,"out","dac"):
#        cnt3 +=1
#    print("c",cnt3)


    #for pth in nx.all_simple_paths(G,"fft","dac"):
    for pth in nx.all_simple_paths(G,"dac","fft"):
        cnt2 +=1
    print("b",cnt2)


    print(nx.has_path(G,"svr","fft"))
    #for pth in nx.all_simple_paths(G,"svr","fft"):
    for pth in nx.all_simple_paths(G,"fft","svr"):
        cnt1 +=1
        print(cnt1)
    print("a",cnt1)

    tst1 = cnt1*cnt2*cnt3
    cnt1=0
    cnt2=0
    cnt3=0

    for pth in nx.all_simple_paths(G,"svr","dac"):
        cnt1 +=1
    print("a",cnt1)
    for pth in nx.all_simple_paths(G,"dac","fft"):
        cnt2 +=1
    print("b",cnt2)
    for pth in nx.all_simple_paths(G,"fft","out"):
        cnt3 +=1
    print("c",cnt3)

    tst2 = cnt1*cnt2*cnt3


print("SUM",tst1,tst2,tst1+tst2)




if False:
    nx.draw(G,with_labels=True)
    plt.show()
    print(G)       
    print("CNT IS",cnt)    

    lights = vals[0][1:-1]
    #light = sum([1<<k if v == '#' else 0 for k,v in enumerate(lights[::-1])]) 
    light = sum([1<<k if v == '#' else 0 for k,v in enumerate(lights)]) 
    joltage = vals[-1]
    buttons = [sum([1<<int(x) for x in v[1:-1].split(',')]) for v in vals[1:-1]]
    
    
    print("lights",lights)
    print("light",light)
    print("joltage",joltage)
    print("buttons",buttons)
    
    
    mincnt = 9999 
    for ii in range(2**len(buttons)):
        tst = 0
        cnt = 0
        print("next")
        for jj in range(len(buttons)):
            if (1<<jj & ii):
                print("yep",jj,buttons[jj],tst,end=" ")
                tst = tst ^ buttons[jj]
                print(tst)
                cnt +=1
                if tst == light:
                    print("cnt is ",cnt)
                    if cnt < mincnt:
                        mincnt = cnt
           
    mincnts.append(mincnt) 

print("sum mincnts ", sum(mincnts))
import pdb
pdb.set_trace()
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



