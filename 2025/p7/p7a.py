import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy

cnt = 0

fp = open(sys.argv[1])

vals = []
cnt = 0
lastline = None
cnt2=0
for line in fp.readlines():
#    print(line,len(line))
    vals = list(line[0:-1])
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
