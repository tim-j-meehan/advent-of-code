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
    import pdb
#    pdb.set_trace()
    vals =  list(line)[0:-1]
    if vals[0] not in ('+','*'):
        print(vals[0])
        #vals = [v if v != " " else 0  for v in vals]
        print(vals)
        #myvals.append([int(v) for v in vals])    
        myvals.append(vals)
    else:
        ops = list(vals)[0:-1]
mymat = np.array(myvals)
cnt=0
v = None
nums = []
tst=0
print(mymat)
for idx,vp in enumerate(ops):
    idx2 = mymat.shape[1] - idx -1
    print(idx,idx2)
    print(mymat.shape)
    print(len(ops),ops)
    vp = ops[idx2]
    print(mymat[:,idx2])
    try:
        nums.append(int("".join(mymat[:,idx2])))
    except:
        print("empty")
    if vp == '+':
        tst = np.sum(nums)
        print("+",nums)
        nums = []
    if vp == '*':
        tst = np.prod(nums)
        print('-',nums)
        nums = []
    
    print("tst",tst)
    cnt += tst
    tst=0
print(cnt)
