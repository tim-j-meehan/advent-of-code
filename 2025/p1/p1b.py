import sys
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib

curpos = 50
fp = open(sys.argv[1])
first = True
cnt = 0
cnt2 = 0
maxp = 0
prevPos = 9
minval = 1000
maxval = -1000
for idx,line in enumerate(fp.readlines()):
    #print(int(line[1:]))
    val = int(line[1:])
    if val < minval:
        minval = val
    if val > maxval:
        maxval = val
    cnt2+= val//100
    val = val %100
    if val%100 == 0:
        import pdb
        pdb.set_trace()
    print("#",curpos,cnt2,val,line[0])
    if 'L' in line:
        curpos -= val
    else:
        curpos += val
    if curpos <=0 and prevPos != 0:
        print("L0")
        cnt2+=1
    if curpos >=100 and prevPos != 0:
        print("H0")
        cnt2+=1
    curpos = curpos%100
    if curpos == 0:
        cnt +=1
    prevPos = curpos
print("cnt",cnt,cnt2,minval,maxval)
