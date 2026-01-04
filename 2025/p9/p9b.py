import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
import networkx as nx
import matplotlib.pyplot as plt
cnt = 0


def check_crossings(aa,bb,mymat):
#    print("aa",aa)
#    print("bb",bb)
    ll = (min(aa[0],bb[0]),min(aa[1],bb[1]))
    ur = (max(aa[0],bb[0]),max(aa[1],bb[1]))
    cross = False
    for ii in range(len(mymat)-1):
        p1 = mymat[ii]
        p2 = mymat[ii+1]
        xmax = max(p1[0],p2[0]) 
        xmin = min(p1[0],p2[0]) 
        ymax = max(p1[1],p2[1]) 
        ymin = min(p1[1],p2[1]) 
        #print(aa,bb,p1,p2, xmin,xmax,ymin,ymax)
        if p1[0] > ll[0] and p1[0] < ur[0] and p1[1] > ll[1] and p1[1] < ur[1]:
            #print("point inside")
            cross = True
            return(cross)

        # horizontal edge 
        if p1[1] == p2[1]:
            # check to see if edge is below top or above bottom 
            if p1[1] < ur[1] and p1[1] > ll[1]:
                # check to see if edge has any points inside box 
                if (p1[0] <= ll[0] and p2[0] >= ur[0]) or\
                   (p2[0] <= ll[0] and p1[0] >= ur[0]):
                    #print("fail1")
                    cross = True

        else:
            # check to see if edge is below top or above bottom 
            if p1[0] < ur[0] and p1[0] > ll[0]:
                # check to see if edge has any points inside box 
                if (p1[1] <= ll[1] and p2[1] >= ur[1])or\
                   (p2[1] <= ll[1] and p1[1] >= ur[1]):
                    #print("fail2")
                    cross = True



    return cross
        
                                       
def invalid(foo):
    N = len(foo)
    if foo[0:N//2] == foo[N//2:N]:
        return int(foo)
    return(0)
fp = open(sys.argv[1])



first = True 
vals = []
cnt = 0
doit = False
myvals = []
lastline = None
cnt2=0
myvals = []

circ = []
for line in fp.readlines():
#    print(line,len(line))
    vals = [int(x) for x in line.split(',')]
    myvals.append(vals)
#    if vals[0] >= 50278:
#        myvals.append(vals)
#    if vals[0] <= 48472:
#        myvals.append(vals)
myvals.append(myvals[0])
mymat = np.array(myvals)
pprint.pprint(mymat)


N = mymat.shape[0]

lookup = {}

mindist = 99999900009
for ii in range(N):
    for kk in range(ii+1,N):
        dif = mymat[ii] - mymat[kk]
        area = abs(dif[0]) * abs(dif[1])
        lookup[area] = (ii,kk) 
#        if dist < mindist:
#            mindist = dist
#            minii= ii
#            minkk=kk

skeys = sorted(lookup.keys())

for ii in range(1,len(skeys)):

    a,b = lookup[skeys[-ii]]
    
#    myvals= ((0,0),(0,3),(2,3),(2,5),(0,5),     (0,8),(8,8),(8,0),(0,0))
#    mymat = np.array(myvals)
#    a = 0
#    b = 6
    val = check_crossings(myvals[a],myvals[b],myvals)
#    val = False
    print(ii,val)
    print(len(myvals))
    if not val:

        plt.plot([m[0] for m in myvals],[m[1] for m in myvals])
        plt.scatter(mymat[a][0],mymat[a][1])
        plt.scatter(mymat[b][0],mymat[b][1])
        print("one corner",mymat[a],"other corner",mymat[b])
        diff = mymat[a] - mymat[b]
        print((abs(diff[0])+1) * (abs(diff[1])+1))

        plt.show()


print("one corner",mymat[a],"other corner",mymat[b])
diff = mymat[a] - mymat[b]
print((diff[0]+1) * (diff[1]+1))



