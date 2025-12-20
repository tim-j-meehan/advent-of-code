from functools import lru_cache
def pmat(mat):
    for nn in range(len(mat)):
        print(''.join(mat[nn]))


@lru_cache
def matchem(line):
    cnt = 0
    #print("len",len(line),line)
    if len(line) == 0:
        #print("ret true")
        return 1 
    for tw in towels:
        #print(line,tw,line.startswith(tw),len(tw),len(line))
        if line.startswith(tw):
            #print("startswith",line,tw)
            #print("line",line[len(tw):])
            cnt += matchem(line[len(tw):])
            #print(cnt)

    #print("reg false")
    return cnt 


