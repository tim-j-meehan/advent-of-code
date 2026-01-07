import sys
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib

fp = open(sys.argv[1])
cnt = 0
for line in fp.readlines():
    vals = [int(i) for  i in line[0:-1]]
    maxv = max(vals[0:-1])
    maxi = vals[0:-1].index(maxv)
    maxv2 = max(vals[maxi+1:])
    cnt += maxv*10 + maxv2
    print(maxv,maxv2) 
    print( vals)
print(cnt)
    
