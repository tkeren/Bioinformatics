import random
import sys
import os
sys.path.append(os.path.abspath("../dataStructures"))
from LinkedList import *
#import LinkedList
'''
def ChromosomeToCycle(c):
    n = len(c)
    nodes = {}
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
'''
def ChromosomeToCycle(c):
    n = len(c)
    ls = LinkedList()
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
    for val in nodes:
        ls.add(val)
    #ls.display()
    return nodes

def CycleToChromosome(nodes):
    n = int(len(nodes)/2)
    #c = nodes.head
#    for i in nodes.size:
 #       print()

    #n = int(nodes.size/2)
    chromosomes = [-1 for i in range(n)]
    for j in range(1,n+1):
        if nodes[(2*j)-2] < nodes[(2*j)-1]:
        #x = nodes.dataAt((2*j)-2)
        #y = nodes.dataAt((2*j)-1)
        #if  x<y:
        #    chromosomes[j - 1] = int(y/2)
            chromosomes[j-1] = int(nodes[(2*j)-1]/2)
        else:
            #chromosomes[j - 1] = int(-1*(x/ 2))
            chromosomes[j-1] = int((-1*(nodes[(2*j)-2]))/2)
    return chromosomes



def coloredEdges(p):
    edges = {}
    for c in p:
        n = ChromosomeToCycle(c)
        for j in range(len(c)):
            #if n[(2*j)-1] in edges:
                #print("yes")
                #x = edges[n[(2*j)-1]]
                #x.add( n[(2*j)])
                #edges[n[(2 * j) - 1]] = x
            #else:
            edges[n[(2 * j) - 1]] = n[(2 * j)]

            #if n[(2 * j)] in edges:
                #x = edges[n[(2 * j)]]
                #x.add(n[(2 * j)-1])
                #edges[n[(2 * j)]] = x
            #else:
            edges[n[(2 * j)]] = n[(2 * j)-1]


    return edges

def blackEdges(p):
    edges = {}
    for c in p:
        n = ChromosomeToCycle(c)
        for j in range(0,2*len(c),2):
            edges[n[j]] = n[j+1]
            edges[n[j+1]] = n[j]
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
                p.append(CycleToChromosome(cycle))
                break
    return p




def breakOnGenomeGraph(g, i1, i2, i3, i4):
    print(g)
    print(i1, i2, i3, i4)
    x = g[i1]
    x.remove(i2)
    x.add(i3)
    g[i1] = x

    x = g[i2]
    x.remove(i1)
    x.add(i4)
    g[i2] = x

    x = g[i3]
    x.remove(i4)
    x.add(i1)
    g[i3] = x

    x = g[i4]
    x.remove(i3)
    x.add(i2)
    g[i4] = x

    return g


''' a = (i1, i2)
    b = (i3,i4)
    ab = (i1, i3)
    ba = (i2,i4)
    for i, j in enumerate(g):
        if j == a:
            g[i] = ab
        if j == b:
            g[j] = ba'''



def breakOnGenome(p, i1, i2, i3, i4):
    be = blackEdges(p)
    ce = coloredEdges(p)
    G = connectGraph(be,ce)
    G = breakOnGenomeGraph(G,i1,i2,i3,i4)
    p = graphToGenome(G)
    return p

def ShortestRearrangment(p, q):
    print(p)
    red = coloredEdges(p)
    blue = coloredEdges(q)
    bg = connectGraph(red, blue)
    #print(bg)
    for c in bg:
        while len(bg[c])>1:#!=bg[bg[c]]:
            #print(bg)
            #r = blue[random.choice(blue)]
            #r = blue[c]
            i1 = c
            i2 = red[c]
            #r = bg[i2]
            i3 = blue[c]
            i4 = red[i3]
            red[i1] = i3
            red[i3] = i1
            red[i2] = i4
            red[i4] = i2
            #print(red)
            #print(blue)
            #bg = blue
            bg = connectGraph(red, blue)
            print(bg)
            p=breakOnGenome(p,i1,i2,i3,i4)
            #print("here")
            print(p)


def breakLength(p,q):
    re = coloredEdges(p)
    be = coloredEdges(q)
    g = connectGraph(be,re)
    l = graphToGenome(g)
    print(l)
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
    breakLength(p,q)
    #ShortestRearrangment(p,q)

#print(CycleToChromosome(ChromosomeToCycle([1,-2,-3,4])))
#x = {1,2,3}
#print(type(x))
#print(blackEdges([[1,-2,-3,4]]))
p = [[1,-2,-3,4]]
q = [[1,2,-4,-3]]
#p = [[1,2,3,4,5,6]]
#q = [[1,-3,-6,-5],[2,-4]]
ShortestRearrangment(p,q)
#breakLength(p,q)
#x.add(5)
#print(x)


#g = {1:{2,3} , 2:{1,3}, 3:{1,2}, 4:{5}, 5:{4} }
#print(graphToGenome(g))
#driver('D:\Projects\Bioinformatics/2-break\data/test.txt')