import sys
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib

def invalid(foo):
    N = len(foo)
    if N == 1:
        return 0
    if foo[0:N//2] == foo[N//2:N]:
        print("GOOD1",foo)
        return int(foo)
    if(len(set(foo)) == 1):
        print("GOOD2",foo)
        return int(foo)
    for KK in range(2,N//2+1):
        good = True
        for kk in range(KK-1):
            #print("TEST",foo)
            #print(foo[kk*N//KK:(kk+1)*N//KK],foo[(kk+1)*N//KK:(kk+2)*N//KK])
            if foo[kk*N//KK:(kk+1)*N//KK] != foo[(kk+1)*N//KK:(kk+2)*N//KK]:
                #print("it false")
                good = False
                break
            else:
                pass
                #print("it true")
        if good:
            print("GOOD3", foo)
            return int(foo)
    return 0        
        
#    if foo[0:N//2] == foo[N//2:N]:
#    if foo[0:N//3] == foo[N//3:2*N//3]:
#    if foo[2*N//3:3*N//3] == foo[N//3:2*N//3]:
#        return int(foo)
#    return(0)
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

print("IS IT",invalid('111'))
