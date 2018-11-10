import numpy as np

def NeighborJoining(D, total, nodename):
    n = len(D)
    if n == 2:
        return {(nodename[0], nodename[1]): D[0][1]}
    ds, td = DStar(D)
    i, j = findMin(ds)
    lmda = (td[i] - td[j])/(n-2)
    lli = (D[i][j] + lmda)/2
    llj = (D[i][j] - lmda) / 2
    D = reformMatrix(D, i, j)

    new = [nn for  pos, nn in enumerate(nodename) if (pos!=i and pos != j)]
    x = total
    new.append(x)
    T = NeighborJoining(D, total+1, new)
    T[(nodename[i], x)] = lli
    T[(nodename[j], x)] = llj
    return T


def DTotal(d):
    result = []
    for i in range(len(d)):
        sum = 0
        for j in range(len(d)):
            sum += d[i][j]
        result.append(sum)
    return result




def DStar(d):
    result = d.copy()
    TD = DTotal(d)
    n = len(d)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            result[i][j] = ((n-2)*d[i][j]) - TD[i] - TD[j]
    return (result, TD)

def findMin(d):
    mi = 0
    mj = 0
    min = 1000
    for i in range(len(d)):
        for j in range(len(d)):
            if j == i:
                continue
            if d[i][j] < min:
                mi = i
                mj = j
                min = d[i][j]
    return (mi, mj)

def reformMatrix(d,ri, rj):
    n = len(d)-1
    matrix = np.zeros((n, n))
    x = 0
    for i in range(n+1):
        y = 0
        if i == ri or i == rj:
            continue
        for j in range(n+1):
            if j == rj or j == ri:
                continue
            matrix[x][y] = d[i][j]
            y+=1
        x+=1
    pos = [i for i in range(0, len(d)) if (i!=rj and i!=ri)]
    for k in range(0,n-1):
        matrix[n-1][k] = (d[ri][pos[k]] + d[rj][pos[k]] - d[ri][rj])/2
        matrix[k] [n - 1] = (d[ri][pos[k]] + d[rj][pos[k]] - d[ri][rj])/2

    return matrix


def driver(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    m = 0
    matrix = []
    for i, line in enumerate(lines):
        if i == 0:
            d = int(line)
            matrix = np.zeros((d,d))
        else:
            l = line.split()
            for j in range(d):
                matrix[i-1][j] = int(l[j])
    nodename = [i for i in range(len(matrix))]
    limb = NeighborJoining(matrix, len(matrix), nodename)
    display(limb)


def display(T):
    result = []
    for i in T:
        s = str(i[0])+"->"+str(i[1])+":"+str(round(T[i],3))
        result.append(s)
        s = str(i[1]) + "->" + str(i[0]) + ":" + str(round(T[i],3))
        result.append(s)
    result = sorted(result, key=lambda x: float(x.split('-')[0]))
    for s in result:
        print(s)

driver('D:\Projects\Bioinformatics\Evolutionary Tree\Data/rosalind_ba7e.txt')