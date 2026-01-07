import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
import networkx as nx
import matplotlib.pyplot as plt
from functools import lru_cache
cnt = 0

fp = open(sys.argv[1])

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
