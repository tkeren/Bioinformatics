from Limb_Length import find_length
import numpy as np

def additivePhylogeny(D, total):
    n = len(D)
    if n == 2:
        return {(0,1):D[0][1]}
    limbLength, i, k = find_length(D, n-1)
    Dtemp = []
    for r, row in enumerate(D):
        if r == n-1:
            continue
        temp = []
        for c, col in enumerate(row):
            if c!=n-1:
                temp.append(col)
        Dtemp.append(temp)

    T = additivePhylogeny(Dtemp, total)
    pack = findPath(T, i, k, ([],[]),set())
    T = addNode(T, limbLength, n-1, D[i][n-1], pack, len(Dtemp) + total - 2)
    return T

def findPath(T, i, k, pack, visited, ):
    path, position = pack
    for limb in T:
        if limb not in visited:
            if limb[0] == i or limb[1] == i:
                temp = path.copy()
                temppos = position.copy()
                if limb[0] == i:
                    temppos.append(0)
                else:
                    temppos.append(1)
                temp.append(limb)
                visited.add(limb)
                if limb[1] == k or limb[0] == k:
                    #print(path)
                    return (temp, temppos)
                else:
                    if limb[0] == i:
                        tpath = findPath(T, limb[1], k, (temp, temppos), visited)
                        if tpath is not None:
                            return tpath
                    if limb[1] == i:
                        t = findPath(T, limb[0], k, (temp, temppos), visited)

                        if t is not None:
                            return t
    #return []


def addNode(T, l, node, total, path, x):
    runner = 0
    for p , ind in zip(*path):
        for limb in T:
            if p[0] == limb[0] and p[1] == limb[1]:
                if runner + T[limb] + l > total:
                    if ind == 1:
                        T[(limb[1], x)] = total - l - runner
                        #print("_______RUNNER_________")
                        #print(matrix[i][node] - runner)
                        # print(T[(limb[0], x)])
                        T[(limb[0], x)] = T[limb] - T[(limb[1], x)]
                        #print(T[(limb[1], x)])
                        T[(node, x)] = l
                        check = False
                        # print("here")
                        del T[(limb[0], limb[1])]
                        return T
                    else:
                        T[(limb[0], x)] = total - l - runner
                        # print("_______RUNNER_________")
                        # print(matrix[i][node] - runner)
                        # print(T[(limb[0], x)])
                        T[(limb[1], x)] = T[limb] - T[(limb[0], x)]
                        #print(T[(limb[0], x)])
                        T[(node, x)] = l
                        check = False
                        # print("here")
                        del T[(limb[0], limb[1])]
                        return T

                else:
                    runner+=T[limb]
                    continue
    #return T



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
       # elif i == 1:
            #m = int(line)
        else:
            l = line.split()
            for j in range(d):
                matrix[i-1][j] = int(l[j])
    #print(matrix, len(matrix))
    limb = additivePhylogeny(matrix, len(matrix))
    display(limb)

def display(T):
    result = []
    for i in T:
        s = str(i[0])+"->"+str(i[1])+" : "+str(int(T[i]))
        result.append(s)
        s = str(i[1]) + "->" + str(i[0]) + " : " + str(int(T[i]))
        result.append(s)
    #result.sort()
    result = sorted(result, key=lambda x: float(x.split('-')[0]))
    for s in result:
        print(s)

driver('D:\Projects\Bioinformatics\Limb_Length\Data/AP2.txt')