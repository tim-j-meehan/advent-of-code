import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../")
import aoclib
import copy

cnt = 0

def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)
fp = open(sys.argv[1])


my_map = {'@':1,'.':0}
mat  = []

first = False 
for line in fp.readlines():
    vals = [my_map[l] for l in line[0:-1]]
#    vals = [0] + vals + [0]
    if first:
        mat.append([0]*len(vals))
        first = False
    mat.append(vals) 

#mat.append([0]*len(vals))

kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
npmat = np.array(mat)




moved = True
while moved: 
    moved = False
    stuf = convolve2d(npmat,kernel)
    print(npmat)
    print(stuf[1:-1,1:-1])
    nstuf=stuf[1:-1,1:-1]
                   

    npmat2 = copy.deepcopy(npmat)

    for ii in range(npmat.shape[0]):
        for kk in range(npmat.shape[1]):
            if npmat[ii][kk] == 0:
                print('.',end='')
            else:
                if nstuf[ii][kk] < 4:
                    print('X',end='')
                    cnt+=1
                    moved = True
                    npmat2[ii][kk] = 0
                else:
                    print("@",end='')
        print()

    print(cnt)
    npmat = copy.deepcopy(npmat2)
