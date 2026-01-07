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
cnt = 0

fp = open(sys.argv[1])

vals = []
cnt = 0
myvals = []

G=nx.DiGraph()

for line in fp.readlines():
    print(line,len(line))
    vals = line.split()
    n_1 = vals[0][:-1]
    for n_x in vals[1:]:
        G.add_edge(n_1,n_x)

for pth in nx.all_simple_paths(G,"you","out"):
    print(pth)
    cnt +=1

nx.draw(G,with_labels=True)
plt.show()
print(G)       
print("CNT IS",cnt)    
