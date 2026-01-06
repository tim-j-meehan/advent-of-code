import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib

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
for line in fp.readlines():
#    print(line,len(line))
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
