import sys
from scipy.signal import convolve2d
import numpy as np
from itertools import combinations
sys.path.append("../../pylib")
import aoclib
import copy
import pprint
import networkx as nx
fp = open(sys.argv[1])

vals = []
cnt = 0
circ = []
mincnts = []
for line in fp.readlines():
    print(line,len(line))
    vals = line.split()
    lights = vals[0][1:-1]
    light = sum([1<<k if v == '#' else 0 for k,v in enumerate(lights)]) 
    joltage = vals[-1]
    buttons = [sum([1<<int(x) for x in v[1:-1].split(',')]) for v in vals[1:-1]]
    print("lights",lights)
    print("light",light)
    print("joltage",joltage)
    print("buttons",buttons)
    mincnt = 9999 
    for ii in range(2**len(buttons)):
        tst = 0
        cnt = 0
        print("next")
        for jj in range(len(buttons)):
            if (1<<jj & ii):
                print("yep",jj,buttons[jj],tst,end=" ")
                tst = tst ^ buttons[jj]
                print(tst)
                cnt +=1
                if tst == light:
                    print("cnt is ",cnt)
                    if cnt < mincnt:
                        mincnt = cnt
           
    mincnts.append(mincnt) 

print("sum mincnts ", sum(mincnts))
