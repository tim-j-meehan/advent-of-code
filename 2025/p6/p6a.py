import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib


fp = open(sys.argv[1])


first = True 
vals = []
doit = False
myvals = []
for line in fp.readlines():
    vals = line.split()
    if vals[0] not in ('+','*'):
        print(vals[0])
        myvals.append([int(v) for v in vals])    
    else:
        ops = vals
mymat = np.array(myvals)
cnt=0
for idx,v in enumerate(ops):
    print(mymat)
    print(mymat[:,idx])
    print(idx,v)
    if v == '+':
        tst = np.sum(mymat[:,idx])
    else:
        tst = np.prod(mymat[:,idx])
    print("tst",tst)
    cnt += tst
print(cnt)
