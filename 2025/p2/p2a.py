import sys
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib

def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)
curpos = 50
fp = open(sys.argv[1])
line = fp.readline()
vals = line.split(',')
cnt = 0
for val in vals:
    (start,stop) = val.split('-')
    for ii in range(int(start),int(stop)+1):
        cnt+=invalid(str(ii))
    print("X",cnt)

    print(start,stop)
print(cnt)
