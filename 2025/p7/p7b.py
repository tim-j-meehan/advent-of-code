import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
from functools import lru_cache



def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)
fp = open(sys.argv[1])


cnt3 = 0


@lru_cache
def doit(ridx,cidx):
    if ridx >= N:
        return 1
    if cidx >= M:
        return 1
    if(myvals[ridx][cidx] == '^'):
        a = 0
        b = 0
        if cidx >= 1:
            a = doit(ridx+1,cidx-1)
        if cidx < M-2:
            b = doit(ridx+1,cidx+1)
        return a+b
         
    else:
        return doit(ridx+1,cidx)

vals = []
myvals = []
idx = 0
for line in fp.readlines():
    vals = list(line[0:-1])
    if idx < 800:
        myvals.append(vals)
    idx +=1
N = len(myvals)
M = len(myvals[0])

for ii in range(len(myvals[0])):
    if myvals[0][ii] == 'S':
        print(N,M)
        full = doit(1,ii)
        print("fULL",full)
        break
