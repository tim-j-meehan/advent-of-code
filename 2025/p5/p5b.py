import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy

cnt = 0

fp = open(sys.argv[1])

def inrange(val,start,stop):
    if val >= start and val <= stop:
        return True
    return False

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
#         [------------------------------------]
#     [----------------]
#     [---]   start = start, stop = val_start

#         [------------------------------------]
#                                  [----------------]
#                                              [----]  stop = stop, start = val_stop

#         [------------------------------------]
#                [----------------]
#         start = stop = Null

#         [------------------------------------]
#     [---------------------------------------------]
#     [---]                                    [----] 
#         start = start, stop = val_start      stop = stop, start = val_Stop


#             [------------------------------------]
#     [----]
#     vals.append(ss)

#             [------------------------------------]
#                                                       [----]
#     vals.append(ss)

        sss = [ss,] 
        if len(vals) == 0:
            vals.append(ss)
        for (start,stop) in vals:
            sssn = []
            for ss in sss:
                print("####")
                print(ss)
                print(start,stop)
                if ss[0] < start and inrange(ss[1],start,stop):
                    sssn.append((ss[0],start-1))
                    break
                elif ss[1] > stop and inrange(ss[0],start,stop):
                    sssn.append((stop+1,ss[1]))
                    break
                elif inrange(ss[0],start,stop) and inrange(ss[1],start,stop):
                    pass
                elif ss[0] < start and ss[1] > stop:
                    sssn.append((ss[0],start-1))
                    sssn.append((stop+1,ss[1]))
                    break
                elif ss[1] < start:
                    sssn.append(ss)
                elif ss[0] > stop:
                    sssn.append(ss)
                else:
                    import pdb
                    pdb.set_trace()
            sss = copy.deepcopy(sssn)
        vals.extend(sss) 
    if not first:
        break

print(vals)
for start, stop in vals:
    cnt += stop-start+1

print("cnt",cnt)
#    vals = [0] + vals + [0]
