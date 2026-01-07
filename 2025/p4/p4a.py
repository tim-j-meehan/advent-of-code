import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib

cnt = 0

fp = open(sys.argv[1])

my_map = {'@':1,'.':0}
mat  = []

first = False 
for line in fp.readlines():
    vals = [my_map[l] for l in line[0:-1]]
    if first:
        mat.append([0]*len(vals))
        first = False
    mat.append(vals) 

#mat.append([0]*len(vals))

# make a kernel 1 1 1
#               1 0 1
#               1 1 1
# and do simple 2d conv

kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
npmat = np.array(mat)
stuf = convolve2d(npmat,kernel)

print(npmat)
print(stuf[1:-1,1:-1])
nstuf=stuf[1:-1,1:-1]
               

# find where there was an orignal roll
#and where hte 2d conv is less than 4
for ii in range(npmat.shape[0]):
    for kk in range(npmat.shape[1]):
        if npmat[ii][kk] == 0:
            print('.',end='')
        else:
            if nstuf[ii][kk] < 4:
                print('X',end='')
                cnt+=1
            else:
                print("@",end='')
    print()

print(cnt)
