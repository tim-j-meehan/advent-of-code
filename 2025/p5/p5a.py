import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib

cnt = 0

fp = open(sys.argv[1])


first = True 
vals = []
cnt = 0
doit = False
for line in fp.readlines():
#    print(line,len(line))
    if len(line) <= 1:
        first = False
    if first:
        ss = [int(s) for s in line.split('-')]
        vals.append(ss)
    if doit:
        val = int(line)  
        for start,stop in vals:
            if val >= start and val <= stop:
                cnt+=1
                print(val,"valid")
                break
    if not first:
        doit = True
print("cnt",cnt)
#    vals = [0] + vals + [0]
