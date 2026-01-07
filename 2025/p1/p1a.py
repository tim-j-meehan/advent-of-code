import sys
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib

curpos = 50
fp = open(sys.argv[1])
first = True
cnt = 0
for idx,line in enumerate(fp.readlines()):
    if 'L' in line:
        curpos -= (int(line[1:]))
    else:
        curpos += (int(line[1:]))
    curpos = curpos%100
    print(curpos)
    if curpos == 0:
        cnt +=1
print("cnt",cnt)
