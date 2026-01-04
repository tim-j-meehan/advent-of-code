import sys
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib

fp = open(sys.argv[1])
cnt = 0
for line in fp.readlines():
    vals = [int(i) for  i in line[0:-1]]

    oldmax =-1 
    thiscnt = 0
    for kk in range(12): 
        jj = 12-(kk)
#        print(jj)
        print(vals)
        print(vals[oldmax+1:len(vals)-(jj-1)])
        maxv = max(vals[oldmax+1:len(vals)-(jj-1)])
        print(jj,kk,maxv,oldmax)
        oldmax = vals[oldmax+1:len(vals)-(jj-1)].index(maxv) + oldmax +1
        print("maxv",maxv,"maxidx",oldmax)
        print(jj,kk,maxv,oldmax)
        thiscnt += maxv * 10**(12-kk-1)
    print(thiscnt)      
    cnt += thiscnt
print(cnt)
    
