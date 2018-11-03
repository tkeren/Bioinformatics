from Limb_Length import find_length
import numpy as np

def additivePhylogeny(D, total):
    n = len(D)
    if n == 2:
        return {(0,1):D[0][1]}
    limbLength, i, k = find_length(D, n-1)
    #print(limbLength)
    '''for j in range(1, n-1):
        D[j][n] = D[j][n] - limbLength
        D[n][j] = D[n][j] - limbLength'''
    # i,n,k <- three leaves such that Di,k = Di,n + Dn,k
    #x = D[i][n]
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
    T = addToTree(T, n-1, limbLength, D, total,i ,k)

    #v <- the (potentially new) node in T at distance x from i on the path between i and k
    # add leaf n back to T by creating a limb (v, n) of length limbLength
    return T


def addToTree(T , node, l, matrix, total,i ,k):
    x = len(matrix) + total - 3
    #print(i,k)
    check = True
    current = i
    runner = 0

    for limb in T:

        if limb[0] == i:
            current = limb[1]
        if (limb[0] == i or limb[0] == k) and matrix[limb[0]][node] - l  <= T[limb]:# and matrix[limb[0]][node] - l<=T[limb]:
            T[(limb[0], x)] = matrix[limb[0]][node] - l
            T[(limb[1], x)] = T[limb] - T[(limb[0], x)]
            if l<0:
                print("here")
            T[(node, x)] = l
            check = False
            del T[(limb[0], limb[1])]
            break

    if check:
            #break
        print("skipped")
        print(node)
        #T = looper(T , node, l, matrix, total,i ,T[limb], current)
        print(T)
            # print(i, k)
            # print(T)
            # print(l)
    return T

def looper(T , node, l, matrix, total,i ,runner, current):
    x = len(matrix) + total - 3
    # print(i,k)
    check = True
    for z in range(total):
        for limb in T:
            if limb[1] == current:
                if matrix[i][node]  <= runner + T[limb] and matrix[i][node]>runner:
                    T[(limb[0], x)] = matrix[i][node] - l - runner
                    print("_______RUNNER_________")
                    print(matrix[i][node] - runner)
                    #print(T[(limb[0], x)])
                    T[(limb[1], x)] = T[limb] - T[(limb[0], x)]
                    T[(node, x)] = l
                    check = False
                    #print("here")
                    del T[(limb[0], limb[1])]
                    return T
                    #break
                else:
                    #print("_______RUNNER_________")
                    #print(matrix[i][node] - runner)
                    #print(current)
                    if True:# limb[0] >= total:
                        test = looper(T , node, l, matrix, total,i ,runner+T[limb], limb[0])
                        if test is not None:
                            return test
    #return (T)


        #if check:
            # break
            #print("skipped")
            #print(node)
            # print(i, k)
            # print(T)
            # print(l)




def find_path(T, i, k, path):
    for limb in T:
        if




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
    result.sort()
    for s in result:
        print(s)

driver('D:\Projects\Bioinformatics\Limb_Length\Data/APtest.txt')