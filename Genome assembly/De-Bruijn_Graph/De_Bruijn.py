def constructGraph(ls):
    kmers = []
    graph = {}
    for line in ls:
        n = len(line)
        k1 = line[0:n-1]
        k2 = line[1:n]
        if k1 not in graph:
            kmers.append(k1)
            graph[k1] = [k2]
        else:
            temp = graph[k1]
            temp.append(k2)
            temp.sort()
            graph[k1] = temp
    kmers.sort()

    return (kmers, graph)


def display(kmers, graph):
    for kmer in kmers:
        s = kmer + ' -> '
        ls = graph[kmer]
        for i in range(len(ls)):
            if i != 0:
                s = s +', ' + ls[i]
            else:
                s = s + ls[i]
        print(s)





def driver(path):
    f = open(path, 'r')
    lines = f.readlines()
    l = lines[0:]
    ls = [i for i in l[0: len(l)]]
    f.close()

    Dna = []
    for i in ls:
        temp =''
        for j in i:
            if j is not '\n':
                temp = temp + j
        Dna.append(temp)
    kmers, graph = constructGraph(Dna)
    display(kmers, graph)



ls = ['GAGG','CAGG', 'GGGG', 'GGGA','CAGG', 'AGGG', 'GGAG']


driver('D:\Projects\Bioinformatics/De-Bruijn_Graph\Data/test.txt')