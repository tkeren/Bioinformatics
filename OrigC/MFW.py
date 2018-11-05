def mfw(s, k):
    D = {}
    for i in range(0,len(s)-k+1):
        kmer = s[i:i+k]
        if kmer in D:
            j = D[kmer]
            D[kmer] = j+1
        else:
            D[kmer] = 1
    mf = []
    count = 0
    for kmer in D:
        if D[kmer] > count:
            mf = [kmer]
            count = D[kmer]
        elif D[kmer] == count:
            mf.append(kmer)
    out = ''
    for o in mf:
        out = out + str(o) + ' '
    out = out[:-1]
    print(out)
    return(out)

mfw('TGTGTATGTTTGGCCTATTTGGCCTATTTGGCCTATGTGTATGATGGAATGTTTTGGCCTATCGACTCTTTGGCCTATTTGGCCTATGTGTATGATCCGAGTCGACTCATCCGAGATGGAATGTTCGACTCATGGAATGTTGTGTATGATGGAATGTATGGAATGTATGGAATGTATGGAATGTATGGAATGTTGTGTATGATGGAATGTTCGACTCTGTGTATGTGTGTATGATGGAATGTATGGAATGTTTTGGCCTATTTGGCCTATCGACTCTGTGTATGATCCGAGTGTGTATGATGGAATGTATGGAATGTTCGACTCATCCGAGTCGACTCTCGACTCTCGACTCATCCGAGTGTGTATGATGGAATGTTGTGTATGATGGAATGTTGTGTATGATGGAATGTATCCGAGTGTGTATGTCGACTCTTTGGCCTATCGACTCTTTGGCCTAATGGAATGTATGGAATGTATGGAATGTTCGACTCATCCGAGTGTGTATGTCGACTCATCCGAGTTTGGCCTATGTGTATGATCCGAGATGGAATGTATGGAATGTTCGACTCTCGACTCATCCGAGTGTGTATGATCCGAGTCGACTCTGTGTATGTGTGTATGATCCGAGATGGAATGTATCCGAGATGGAATGTATCCGAGATCCGAGTTTGGCCTAATGGAATGTTTTGGCCTATCGACTCTCGACTCATCCGAGTTTGGCCTATCGACTCTGTGTATGTGTGTATGATCCGAGATGGAATGTATGGAATGTTTTGGCCTATCGACTCTTTGGCCTATGTGTATGTTTGGCCTAATGGAATGTTCGACTCATCCGAGATGGAATGT', 13)

