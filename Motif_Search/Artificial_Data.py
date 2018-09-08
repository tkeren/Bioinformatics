import random
import csv

vocab = ['A', 'T', 'G', 'C']
for i in range(0,200):
    l = []
    s = ''
    for j in range(0,2000):
        #l.append(random.choice(vocab))
        if j != 0:
            s = s +','
        s = s + random.choice(vocab)

    with open('D:/Projects/Bioinformatics/Motif_Search/test_data/Data_' + str(i)+'.csv', 'w') as f:
        #writer = csv.writer(f)
        f.write(s)
        f.close()
