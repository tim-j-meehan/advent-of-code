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
from functools import lru_cache
import re
import doctest
cnt = 0

cnt = 0
doit = False
lastline = None
cnt2=0

circ = []
mincnts = []

G=nx.DiGraph()
#for ii in range(N):
#    G.add_node(ii)
    

def create_aux_shapes(shapes):
    '''Create a set of auxiliary shapes that are square combincations    
   
    '''        
        

def doit():
    fcnt=0
    fp = open(sys.argv[1])
    ncnt = {}
    state = None
    shapes = []
    regions = []

    plt.ion()  # interactive mode on
    fig, ax = plt.subplots()
    im = None  # we'll create this once we have a matrix to show


    for line in fp.readlines():
        print("state", state)
        if state == 'shape':
            if len(line) > 1:
                shape.append([0 if v=='.' else 1 for v in line[:-1]])     
                print(shape)
            else:
                state = None            
                shapes.append(np.array(shape))
        numbers = re.findall(r'^(\d+):', line)
        print(line)
        print("numbers",numbers)
        if(len(numbers)>0):
            shape = []
            state='shape'
        dim = re.findall(r'^(\d+)x(\d+):(( \d+)+)', line)
        if(len(dim) > 0):
            print(dim[0])
            dd = dim[0]
            regions.append((np.zeros((int(dd[0])+1,int(dd[1])+1)),[int(d) for d in dd[2].split()]))        

    ashapes = create_aux_shapes(shapes)

    for reg in regions:
        #print(reg)
        fit = True
        mymat = reg[0]

        if im is None:
            im = ax.imshow(mymat, interpolation="nearest", origin="upper")
            ax.set_title("Live update")
            fig.canvas.draw()
            plt.show(block=False)
        else:
            im.set_data(mymat)

        shape_area = 0
        shape_max_area = 0
        for idx,num in enumerate(reg[1]):
            for idx2 in range(num): # each shape added multiple times
                shape_area += np.sum(shapes[idx])
                shape_max_area += (cur_extent(shapes[idx])[1])
        reg_area = mymat.shape[0] * mymat.shape[1]
        print("possible?",shape_area,shape_max_area,reg_area)
        # Below is just a simple min /max bound that ended up getting me
        # the correct answer
        if True:        
            if shape_area > reg_area:
                print("nope")
                continue
            elif shape_max_area < reg_area:
                print("yep")
                fcnt += 1
                continue
            else:
                print("not sure")
                continue

        for idx,num in enumerate(reg[1]):
            for idx2 in range(num): # each shape added multiple times
                fit = fit and  add_shape(mymat,shapes[idx])

                im.set_data(mymat)
                im.set_clim(vmin=np.min(mymat), vmax=np.max(mymat))
                fig.canvas.draw_idle()
                plt.pause(0.01)

        if fit:
            fcnt +=1
    print(fcnt, len(regions))


def cur_extent(mymat):
    """
    >>> vals = cur_extent(np.array(((0,1),(0,0),(1,1))))
    >>> assert vals == (0,2,0,1)
    """    
    cnt = 0
    idxs = np.nonzero(np.sum(mymat,1))[0]
    cnt += sum(idxs)
    minx = idxs[0]
    maxx = idxs[-1]
    idxs = np.nonzero(np.sum(mymat,0))[0]
    cnt += sum(idxs)
    miny = idxs[0]
    maxy = idxs[-1]
    return(cnt,(maxx+1)*(maxy+1),(maxx-minx)*(maxy-miny),minx,maxx,miny,maxy)

def calc_metric(mymat):
    pass

def add_shape(mymat,shp):
    ''' greedy add of shp to the array '''    
#    minx,maxx,miny,maxy = cur_extent(mymat)
    N = mymat.shape[0]
    M = mymat.shape[1]

    #print(N,M) 
    mf=mi=mk=mr = 0
#    tmat = mymat
    mincur = 9999
    for flip in (0,1): 
        for ridx in range(4):
            tshp = np.rot90(shp,ridx)
            if flip:
                tshp = np.flipud(tshp)
            for ii in range(N-tshp.shape[0]):
                for kk in range(M-tshp.shape[1]):
                    tmat = copy.deepcopy(mymat)
                    tmat[ii:ii+tshp.shape[0],kk:kk+tshp.shape[1]] += tshp
                    if np.max(tmat) > 1:
#                        tmat[ii:ii+tshp.shape[0],kk:kk+tshp.shape[1]] -= tshp
                        continue
#                    tmat[ii:ii+tshp.shape[0],kk:kk+tshp.shape[1]] -= tshp
                    cur = cur_extent(tmat)[0]
                    if cur < mincur:
                        mincur = cur
                        mi=ii
                        mk=kk
                        mr=ridx
                        mf=flip
#                        plt.imshow(tmat)
#                        plt.show()
                    #print(cur)
    if mincur != 9999:
        tshp = np.rot90(shp,mr)
        if mf:
            tshp = np.flipud(tshp)
        mymat[mi:mi+tshp.shape[0],mk:mk+tshp.shape[1]] += tshp
#        plt.imshow(mymat)
#        plt.show()
        return True
    else:
        print("no dice")
        return False
    
# turn on for visualization
if False:
    print(shapes)
    for shp in shapes:
        plt.imshow(shp)
        plt.show()
    

if __name__ == '__main__':
#    doctest.testmod()
    doit()

