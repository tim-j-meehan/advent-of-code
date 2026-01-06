import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib
import copy
import pprint
from functools import lru_cache


cnt = 0

def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)
fp = open(sys.argv[1])


cnt3 = 0


@lru_cache
def doit(ridx,cidx):
#    print(ridx,cidx)
    if ridx >= N:
        return 1
    if cidx >= M:
        return 1
    #print("@",ridx,N,cidx,M)
    if(myvals[ridx][cidx] == '^'):
        #print(cnt3)
        a = 0
        b = 0
        if cidx >= 1:
            a = doit(ridx+1,cidx-1)
        if cidx < M-2:
            b = doit(ridx+1,cidx+1)
        return a+b
         
    else:
        return doit(ridx+1,cidx)

first = True 
vals = []
cnt = 0
myvals = []
lastline = None
cnt2=0
idx = 0
for line in fp.readlines():
#    print(line,len(line))
    vals = list(line[0:-1])
    if idx < 800:
        myvals.append(vals)
    idx +=1
N = len(myvals)
M = len(myvals[0])
#pprint.pprint(myvals)

for ii in range(len(myvals[0])):
    if myvals[0][ii] == 'S':
        print(N,M)
        full = doit(1,ii)
        print("fULL",full)
        break
print("cNT#",cnt3)
if False:
    print(lastline)
    if lastline is None:
        lastline = vals
    else:
        for idx,val in enumerate(vals):
            if val == '.':
                if lastline[idx] in ('|','S'):
                    cnt +=1
                    vals[idx] = '|'       
            elif val == '^':
                if lastline[idx] in ('|','S'):
                    cnt2+=1
                    if vals[idx-1] == '.':
                        vals[idx-1] = '|'
                        cnt +=1
                    if vals[idx+1] == '.':
                        vals[idx+1] = '|'
                        cnt +=1
            else:
                pass
    lastline = copy.deepcopy(vals)
print(cnt,cnt2)
        
