import numpy as np
import random


def getRandom(DNAlist, k):
    l = len(DNAlist)
    Kmers = [[] for i in range(0, len(DNAlist))]
    num = 0
    vals =[]
    for strand in DNAlist:
        n = len(strand)-k
        randVal = random.sample(range(0,n+1),1)[0]
        vals.append(randVal)
        substring = strand[randVal:randVal+k]
        Kmers[num].append(substring)
        num+=1
    motifs = np.vstack(Kmers)
    score = 0
    bestMotifs = []
    while(True):
        profile = makeProfile(motifs)
        bestMotifs = findMOTIF(DNAlist, profile)
        bestprofile = makeProfile(bestMotifs)
        bestScore = getscore(bestMotifs,bestprofile)
        score = getscore(motifs, profile)
        if  bestScore < score:
            motifs = bestMotifs.copy()
        else:
            break
    return(bestMotifs, score)


def makeProfile(DNA):
    l = len(DNA[0])
    #print(DNA)
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


def findMOTIF(DNA, profile):
    #print(profile)
    k = len(profile[0])
    kmers = []
    strandNum = 0
    for strand in DNA:
        mostFrequentVal = 0.0
        mostFrequent = ''

        for i in range(0, len(strand)-k):
            temp = 1
            for j in range(0, k):
                if strand[i+j] == 'A':
                    temp = temp * profile[0][j]
                elif strand[i+j] == 'C':
                    temp = temp * profile[1][j]
                elif strand[i+j] == 'G':
                    temp = temp * profile[2][j]
                else:
                    temp = temp * profile[3][j]
            if temp >= mostFrequentVal:
                mostFrequentVal = temp
                mostFrequent = strand[i:i+k]
        kmers.append(mostFrequent)
        strandNum+=1
    kmers = np.vstack(kmers)

    return kmers


def getscore(motifs, profile):
    letters = ['A', 'C','G', 'T']
    common = ''
    for i in range(0, len(profile[0])):
        arr = []
        for j in range(0,4):
            arr.append(profile[j][i])
        indx = np.argmax(arr)
        common = common + letters[indx]

    score = 0
    for motif in motifs:
        for g in range(len(motif)):
            if motif[g] != common[g]:
                score += 1
    return score


def Drive(ls, k):
    Dna = []
    for i in ls:
        temp = []
        for j in i:
            if j is not '\n':
                temp.append(j)
        Dna.append(temp)

    motifs, score = getRandom(Dna, k)
    for i in range(0, 1000):
        bestmotifs, bestscore = getRandom(Dna, k)
        if bestscore < score:
            print('Lowest score detected: ' + str(bestscore))
            motifs = bestmotifs.copy()
            score = bestscore

    for motif in motifs:
        p = ''
        for i in motif:
            p = p + i
        print(p)
    print("With score: " + str(score))



def getDnaFromFile(path):
    f = open(path, 'r')
    lines = f.readlines()
    l = lines[1:]
    ls = [i for i in l[0: len(l)]]
    f.close()
    return ls



Drive(getDnaFromFile('D:\Projects\Bioinformatics\Motif_Search\Data\Randomized.txt'), 20)
