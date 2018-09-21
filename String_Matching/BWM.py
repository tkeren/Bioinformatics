def importData(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    Last = lines[0]
    patterns = lines[1].split(" ")
    return (list(Last), patterns)

def BurrowsWheeler(s):
    matrix = []
    n = len(s)
    for i in range(1,n+1):
        temp = s[-i:]
        temp+=s[:n-i]
        matrix.append(temp)
    matrix.sort()
    bwt = ''
    for m in matrix:
        bwt = bwt + m[n-1]
    return bwt



def LastToFirst(s, p):
    first = list(s).copy()
    first.sort()
    skip = 0
    for i in range(0,p):
        if s[i] == s[p]:
            skip+=1
    m = s[p]
    for i, j in enumerate(first):
        if j == m:
            if skip == 0:
                return (i)
            else:
                skip-=1


def BWMatching(First, Last, pattern):
    top = 0
    bottom = len(Last)-2
    while top <= bottom:
        if len(pattern)!=0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            found = False
            topindex = -1
            bottomindex = -1
            for i in range(top-1, bottom):
                if Last[i] == symbol:
                    found = True
                    if topindex == -1:
                        topindex = i
                    bottomindex = i
            if found:
                top = LastToFirst(Last, topindex)
                bottom = LastToFirst(Last, bottomindex)
            else:
                return 0
        else:
            return bottom-top + 1


def BWNDriver(Last, patterns):
    First = Last.copy()
    First.sort()
    s = ""
    for p in patterns:
        s = s + str(BWMatching(First, Last, p))+ ' '
    s = s[:-1]
    print(s)



Last, patterns = importData('D:\Projects\Bioinformatics\String_Matching\Data/data.txt')
BWNDriver(Last, patterns)