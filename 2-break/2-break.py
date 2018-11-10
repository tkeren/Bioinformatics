

def ChromosomeToCycle(c):
    n = len(c)
    nodes = [0 for i in range(0, (2*n))]
    j = 0
    for i in c:
        j+=1
        if i > 0:
            nodes[(2*j)-2] = (2*i)-1
            nodes[(2 * j)-1] = (2 * i)
        else:
            nodes[(2 * j) - 2] = -1 * (2 * i)
            nodes[(2 * j)-1] = (-1*(2 * i)) - 1
    return nodes

def CycleToChromosome(nodes):
    n = int(len(nodes)/2)
    chromosomes = [-1 for i in range(n)]
    for j in range(1,n+1):
        if nodes[(2*j)-2] < nodes[(2*j)-1]:
            chromosomes[j-1] = int(nodes[(2*j)-1]/2)
        else:
            chromosomes[j-1] = int((-1*(nodes[(2*j)-2]))/2)
    return chromosomes



def coloredEdges(p):
    edges = {}
    for c in p:
        n = ChromosomeToCycle(c)
        for j in range(len(c)):
            edges[n[(2 * j) - 1]] = n[(2 * j)]
            edges[n[(2 * j)]] = n[(2 * j)-1]

    return edges

def blackEdges(p):
    edges = {}
    n = 0
    for c in p:
        n += len(c)

    for i in range(1,(2*n)+1,2):
        edges[i] = i+1
        edges[i+1] = i
    return edges


def graphToGenome(g):
    p = []
    visited = set()


    for i in range(0,len(g)+1):
        if i not in g:
            continue
        cycle = []
        j = i
        while True:
            cycle.append(j)
            visited.add(j)
            x = g[j]
            v= True
            for s in x:
                if s not in visited:
                    v = False
                    del g[j]
                    j = s
                    break
            if v:
                del g[j]
                if abs(cycle[0]-cycle[-1]) == 1:
                    temp = [cycle[-1]]
                    for q in range(len(cycle)-1):
                        temp.append(cycle[q])
                    cycle=temp
                p.append(CycleToChromosome(cycle))
                break
    return p










def breakOnGenome(p, i1, i2, i3, i4):
    be = blackEdges(p)
    ce = coloredEdges(p)
    ce[i1] = i3
    ce[i3] = i1
    ce[i2] = i4
    ce[i4] = i2
    G = connectGraph(be,ce)
    p = graphToGenome(G)
    return p

def ShortestRearrangment(p, q):
    print("from: ")
    display(p)
    print("to: ")
    display(q)
    print("________________________________")
    display(p)
    red = coloredEdges(p)
    blue = coloredEdges(q)
    bg = connectGraph(red, blue)
    for c in bg:
        while len(bg[c])!=1:

            i1 = c
            i2 = red[c]
            i4 = blue[c]
            i3 = red[i4]
            red[i1] = i4
            red[i4] = i1
            red[i2] = i3
            red[i3] = i2
            bg = connectGraph(red, blue)
            p=breakOnGenome(p,i1,i2,i4,i3)
            display(p)


def breakLength(p,q):
    re = coloredEdges(p)
    be = coloredEdges(q)
    g = connectGraph(be,re)
    l = graphToGenome(g)
    n = 0
    for i in p:
        n += len(i)
    print(n - len(l))

def connectGraph(s1, s2):
    g = {}
    for i in s1:
        x = s2[i]
        y = {s1[i]}
        y.add(x)
        g[i] = y
    return g


def display(p):
    result = ''
    for c in p:
        s = '('
        for j, i in enumerate(c):
            if i >0:
                if j == len(c)-1:
                    s = s + '+'+str(i)+ ')'
                else:
                    s = s + '+'+str(i)+ ' '
            else:
                if j == len(c)-1:
                    s = s +str(i)+ ')'
                else:
                    s = s +str(i)+ ' '
        result+=s
    print(result)



def driver(path):
    f = open(path, 'r')
    lines = f.readlines()
    p=[]
    q=[]
    s= ""
    for j, line in enumerate(lines):
        for c in line:
            if c == ')':
                x = s.split(' ')
                x = [int(i) for i in x]
                if j == 0:
                    p.append(x)
                else:
                    q.append(x)
                s = ""
            elif c == '(':
                continue
            else:
                s+=c
    #breakLength(p,q)
    ShortestRearrangment(p,q)


p = [[1,-5, -4, 2, 3, 7, 6, 8]]
q = [[1,2,3,4, 5, 6, 7, 8]]
ShortestRearrangment(p,q)
#breakLength(p,q)

#driver('D:\Projects\Bioinformatics/2-break\data/test2.txt')
