from collections import defaultdict
import numpy as np
class graph:
    def __init__(self):
        self.val = 0
        self.edges = defaultdict(list)
        self.v = defaultdict(int) #contains outgoing edges - incoming edges

    #add edge to graph
    def addEdges(self, u, v):
        #add edge u - v to edges
        if u not in self.edges:
            self.edges[u] = [v]
        else:
            temp = self.edges[u]
            temp.append(v)
            self.edges[u] = temp
        #add 1 to u outgoing edges
        if u not in self.v:
            self.v[u] = 1
        else:
            temp = self.v[u]
            temp +=1
            self.v[u] = temp
        #remove 1 from outgoing edges
        if v not in self.v:
            self.v[v] = -1
        else:
            temp = self.v[v]
            temp -=1
            self.v[v] = temp
        self.val += 1

    #remove edge from graph
    def removeEdge(self,u , v):
        temp = self.edges[u]
        if len(temp) == 1:
            self.edges.pop(u)
        else:
            ntemp = [i for i in temp if i != v]
            self.edges[u] = ntemp
        self.val -= 1

    #finds the eulerian path or circuit
    def findPath(self,u):
        stack=[]
        path = []
        end = self.val+1
        while(True):
            if len(self.edges[u]) == 0:
                path.append(u)
                if len(path) == end:
                    return (path)
                u = stack.pop()
            else:
                stack.append(u)
                v = self.edges[u][0]
                self.removeEdge(u,v)
                u = v



    def containsPath(self):
        odds = []
        even = []
        for v in self.v:
            if self.v[v] == 1:
                odds.append(v)
            if self.v[v] == 0:
                even.append(v)
        if len(odds) == 1:
            print('eulerian path: ')
            return odds[0]
        elif len(even)== len(self.v):
            print('Eulerian circuit:')
            return even[0]
        else:
            print('The graph does not contain an eulerian path or circuit')
            return None




    def driver(self):
        s = []
        u = self.containsPath()
        if u is None:
            return
        else:
            s = self.findPath(u)
        s.reverse()
        result = ''
        for i in range(len(s)):
            if i == 0:
                result = result +  str(s[i])
            else:
                result = result + '->' + str(s[i])
        print(result)


# form a graph from from a text file in an adjecency format
def formGraph(path):
    g = graph()
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.replace(" ","")
        line = line.replace('>',"")
        u = ''
        v = ''
        first = False
        for n in line:
            if not first:
                if n == '-':
                    u = int(u)
                    first = True
                else:
                    u += n
            else:
                if n == ',':
                    v = int(v)
                    g.addEdges(u,v)
                    v = ''
                else:
                    v = v + n
        g.addEdges(u, int(v))
        u = ''
        v = ''
    return g








'''
g = graph()

g.addEdges(0, 2)
g.addEdges(1, 3)
g.addEdges(2, 1)
g.addEdges(3, 0)
g.addEdges(3, 4)
g.addEdges(6, 3)
g.addEdges(6, 7)
g.addEdges(7, 8)
g.addEdges(8, 9)
g.addEdges(9, 6)'''


'''g.addEdges(1, 2)
g.addEdges(2, 3)
g.addEdges(3, 4)
g.addEdges(4, 1)'''

g = formGraph('D:\Projects\Bioinformatics\Eulerian Path\Data/test.txt')
g.driver()


