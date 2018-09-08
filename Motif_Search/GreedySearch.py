import numpy as np


def GreedySearch(Dna, k, t):
    BestMotifs = []
    for strand in Dna:
        BestMotifs.append(strand[0:k])


    l = len(Dna[0])
    for i in range(0,l-k):
        kmer = Dna[0][i:i+k]
        motifs = [kmer]
        for j in range(1, t):
            profile = makeProfile(motifs)
            motifs.append(mostProbable(profile, Dna[j]))
        if greedyscore(motifs)<greedyscore(BestMotifs):
            BestMotifs = motifs.copy()
    return BestMotifs


def mostProbable(profile, strand):
    commonscore = 0
    k = len(profile[0])
    common = strand[0:k]

    for i in range(0,len(strand)-k):
        kmer = strand[i:i+k]
        tempScore = 1
        for j in range(0,len(kmer)):
            if kmer[j] == 'A':
                tempScore = tempScore * profile[0][j]
            elif kmer[j] == 'C':
                tempScore = tempScore * profile[1][j]
            elif kmer[j] == 'G':
                tempScore = tempScore * profile[2][j]
            else:
                tempScore = tempScore * profile[3][j]
        if tempScore>commonscore:
            common = kmer.copy()
            commonscore = tempScore
    return common


def greedyscore(motifs):
    profile = makeProfile(motifs)
    letters = ['A', 'C','G', 'T']
    common = []
    for i in range(0, len(profile[0])):
        arr = []
        for j in range(0,4):
            arr.append(profile[j][i])
        indx = np.argmax(arr)
        common.append(letters[indx])

    score = 0
    for motif in motifs:
        for g in range(len(motif)):
            if motif[g] != common[g]:
                score += 1
    return score


def makeProfile(DNA):
    l = len(DNA[0])
    for i in DNA:
        if len(i) != l:
            print("ERR. length of k-mers doesnt match. " + str(l) + ' != ' + str(len(i)))
    profile = [[],[],[],[]]
    for i in range(0,l):
        A = 0
        C = 0
        G = 0
        T = 0
        for strand in DNA:
            if strand[i] == 'A':
                A +=1
            elif strand[i] == 'C':
                C +=1
            elif strand[i] == 'G':
                G +=1
            else:
                T+=1
        sum = A+G+C+T
        profile[0].append(A/sum)
        profile[1].append(C/sum)
        profile[2].append(G/sum)
        profile[3].append(T/sum)
    return profile


def greedyDrive(ls, k, t,):
    Dna = []
    for i in ls:
        temp = []
        for j in i:
            if j is not '\n':
                temp.append(j)
        Dna.append(temp)
    result = GreedySearch(Dna, k, t)
    for line in result:
        s =""
        for c in line:
            s = s + c
        print(s)


def getDnaFromFile(path):
    f = open(path, 'r')
    lines = f.readlines()
    l = lines[1:]
    ls = [i for i in l[0: len(l)]]
    f.close()
    return ls




greedyDrive(getDnaFromFile('D:\Projects\Bioinformatics\Motif_Search\Data\Greedy.txt'), 12, 25)