import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib

cnt = 0
fp = open(sys.argv[1])
vals = []
doit = False
myvals = []
for line in fp.readlines():
    vals =  list(line)[0:-1]
    if vals[0] not in ('+','*'):
        print(vals[0])
        print(vals)
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
