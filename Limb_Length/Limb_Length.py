import numpy as np


def find_length(matrix, i):
    m = len(matrix)
    minlimb = 10000
    for j in range(m):
        if j == i:
            continue
        k = 0
        for indx in range(m):
            if indx != i and indx!=j:
                k = indx
                break

        limb = (matrix[i][k] + matrix[i][j] - matrix[j][k])/2
        if limb<minlimb:
            minlimb = limb
    return minlimb


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
        elif i == 1:
            m = int(line)
        else:
            l = line.split()
            for j in range(d):
                matrix[i-2][j] = int(l[j])

    limb = find_length(matrix, m)
    print(limb)



#driver('D:\Projects\Bioinformatics\Limb_Length\Data/tree.txt')