from Limb_Length import *
def additivePhylogeny(D, n):
    if n == 2:
        return
    limbLength = find_length(D, n)
    for j in range(1, n-1):
        D[j][n] = D[j][n] - limbLength
        D[n][j] = D[n][j] - limbLength
    # i,n,k <- three leaves such that Di,k = Di,n + Dn,k
    x = D[i][n]
    Dtemp = []
    for r, row in enumerate(D):
        if r == n:
            continue
        temp = []
        for c, col in enumerate(row):
            if c!=n:
                temp.append(col)
        Dtemp.append(temp)

    T = additivePhylogeny(Dtemp, n-1)
    #v <- the (potentially new) node in T at distance x from i on the path between i and k
    # add leaf n back to T by creating a limb (v, n) of length limbLength
    return T





