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
import re
import doctest
cnt = 0

def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)



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
    

def doit():
    fp = open(sys.argv[1])
    ncnt = {}
    state = None
    shapes = []
    regions = []
    for line in fp.readlines():
        if state == 'shape':
            if len(line) > 1:
                shape.append([0 if v=='.' else 1 for v in line[:-1]])     
                print(shape)
            else:
                state = None            
                shapes.append(np.array(shape))
        numbers = re.findall(r'^(\d+):', line)
        print(numbers)
        if(len(numbers)>0):
            shape = []
            state='shape'
        dim = re.findall(r'^(\d+)x(\d):(( \d+)+)', line)
        if(len(dim) > 0):
            print(dim[0])
            dd = dim[0]
            regions.append((np.zeros((int(dd[0]),int(dd[1]))),[int(d) for d in dd[2].split()]))        

    for reg in regions:
        print(reg)
        mymat = reg[0]
        for idx,num in enumerate(reg[1]):
            for idx2 in range(num): # each shape added multiple times
                for ridx in range(4):
                    add_shape(mymat,np.rot90(shapes[idx],ridx))




def cur_extent(mymat):
    """
    >>> vals = cur_extent(np.array(((0,1),(0,0),(1,1))))
    >>> assert vals == (0,2,0,1)
    """    
    idxs = np.nonzero(np.sum(mymat,1))[0]
    #print(idxs)
    minx = idxs[0]
    maxx = idxs[-1]
    idxs = np.nonzero(np.sum(mymat,0))[0]
    miny = idxs[0]
    maxy = idxs[-1]
#    print(minx,maxx,miny,maxy)
    return(minx,maxx,miny,maxy)

def add_shape(mymat,shp):
    ''' greedy add of shp to the array '''    
#    minx,maxx,miny,maxy = cur_extent(mymat)
    N = mymat.shape[0]
    M = mymat.shape[1]

    print(N,M)
    for ii in range(N-shp.shape[0]):
        for kk in range(M-shp.shape[1]):
            tmat = copy.deepcopy(mymat)
            tmat[ii:ii+shp.shape[0],kk:kk+shp.shape[1]] += shp
            plt.imshow(tmat)
            plt.show()

    
if False:
    print(shapes)
    for shp in shapes:
        plt.imshow(shp)
        plt.show()
    

if __name__ == '__main__':
    doctest.testmod()
    doit()

