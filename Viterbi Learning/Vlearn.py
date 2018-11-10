import numpy as np
class Vlearn:


    def __init__(self):
        self.iterations = None
        self.observations = None
        self.states = None
        self.emission = None
        self.transitions = None
        self.alphabet = None
        self.ab = None
        self.fromText('D:\Projects\Bioinformatics\Viterbi Learning\data/d3.txt')
        path = self.probable_path()
        transition, emission = self.findET(path)
        while not np.array_equal(transition, self.transitions): # and emission.all() != self.emission.all():
            #print('here')
            self.transitions = transition
            self.emission = emission
            path = self.probable_path()
            transition, emission = self.findET(path)
        #print(emission)
        #print(transition)
        self.display()

    def probable_path(self):
        weights = np.zeros((self.iterations, len(self.states)))
        for i, p in enumerate(self.observations):
            for s in range (len(self.states)):
                if i == 0:
                    if self.emission[s][self.ab[p]] == 0:
                        weights[i][s] = -10000000.0
                    else:
                        weights[i][s] = np.log2(self.emission[s][self.ab[p]])#todo:check order
                else:
                    temp = []
                    for j in range(len(self.states)):
                        if self.transitions[j][s] * self.emission[s][self.ab[p]] == 0:
                            x = -10000000.0
                        else:
                            x = weights[i-1][j] + np.log2(self.transitions[j][s] * self.emission[s][self.ab[p]])
                        temp.append(x)
                    weights[i][s] = np.max(temp)
        path = []
        for i in range(0, len(self.observations)):
            x = len(self.observations)-1-i
            if i == 0:
                path.append(np.argmax(weights[x]))
            else:
                temp = []
                for j in range(len(self.states)):
                    #print(self.transitions[j][temp[-1]])
                    if self.transitions[j][path[-1]] * self.emission[path[-1]][self.ab[self.observations[x+1]]] == 0:
                        val = -10000000.0
                    else:
                        val = weights[x][j] + np.log2(self.transitions[j][path[-1]] * self.emission[path[-1]][self.ab[self.observations[x+1]]])
                    temp.append(val)
                path.append(np.argmax(temp))
        path.reverse()
        #print(path)
        self.findET(path)
        return path

    def findET(self, path):
        transitions = np.zeros(self.transitions.shape)
        for s in range(len(path)-1):
            transitions[path[s]][path[s+1]] += 1
        #print(transitions)
        for i in range(len(transitions)):
            s = np.sum(transitions[i])
            for j in range(len(transitions[i])):
                if s == 0:
                    transitions[i][j] = 0.0
                else:
                    transitions[i][j] = round(transitions[i][j]/s,3)
        #print(transitions)

        emission = np.zeros(self.emission.shape)
        for s in range(len(path)):
            emission[path[s]][self.ab[self.observations[s]]] += 1
        # print(transitions)
        for i in range(len(emission)):
            s = np.sum(emission[i])
            for j in range(len(emission[i])):
                if s == 0:
                    emission[i][j] = 0.0
                else:
                    emission[i][j] = round(emission[i][j] / s, 3)
        #print(emission)

        return transitions, emission



    def fromText(self, path):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        m = 0
        counter = 0
        #transition = None
        #emission = None
        for line in lines:
            line = line.rstrip()
            if line == "--------":
                m+=1
                continue
            if m == 0:
                self.iterations = int(line)
            if m == 1:
                self.observations = list(line)
            if m == 2:
                #l = line.split('   ')
                l = line.split('	')
                self.alphabet = l
                ab = {}
                for j, letter in enumerate(l):
                    ab[letter] = j
                self.ab = ab
            if m == 3:
                #self.states = line.split('   ')
                self.states = line.split('	')
                transition = np.zeros((len(self.states),len(self.states)))
                emission = np.zeros((len(self.states), len(self.ab)))
            if m == 4:
                m+=1
                continue
            if m == 5:
                l = line.split('	')
                for j, s in enumerate(l):
                    if j == 0:
                        continue

                    transition[counter][j-1] = float(s)
                counter+=1

            if m == 6:
                m+=1
                counter = 0
                continue

            if m == 7:
                l = line.split('	')
                for j, s in enumerate(l):
                    if j == 0:
                        continue
                    emission[counter][j-1] = float(s)
                counter+=1
        self.transitions = transition
        self.emission = emission


    def fromText2(self, path):
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        m = 0
        counter = 0
        #transition = None
        #emission = None
        for line in lines:
            line = line.rstrip()
            if line == "--------":
                m+=1
                continue
            if m == 0:
                self.iterations = int(line)
            if m == 1:
                self.observations = list(line)
            if m == 2:
                l = line.split('   ')
                #l = line.split(' ')
                ab = {}
                for j, letter in enumerate(l):
                    ab[letter] = j
                self.ab = ab
            if m == 3:
                self.states = line.split('   ')
                #self.states = line.split(' ')
                transition = np.zeros((len(self.states),len(self.states)))
                emission = np.zeros((len(self.states), len(self.ab)))
            if m == 4:
                m+=1
                continue
            if m == 5:
                l = line.split('   ')
                for j, s in enumerate(l):
                    if j == 0:
                        continue

                    transition[counter][j-1] = float(s)
                counter+=1

            if m == 6:
                m+=1
                counter = 0
                continue

            if m == 7:
                l = line.split('   ')
                for j, s in enumerate(l):
                    if j == 0:
                        continue
                    emission[counter][j-1] = float(s)
                counter+=1
        self.transitions = transition
        self.emission = emission

    def display(self):
        p = '   '
        for s in range(len(self.states)):
            if s == len(self.states)-1:
                p+=self.states[s]
            else:
                p += self.states[s] + ' '
        print(p)

        p = ''
        for s in range(len(self.states)):
            p+=self.states[s]+' '
            for j in range(len(self.states)):
                if j == len(self.states) - 1:
                    p += str(self.transitions[s][j])
                else:
                    p = p + str(self.transitions[s][j]) + ' '
            if s != len(self.states)-1:
                p+='\n'

        print(p)

        print('--------')

        p = '   '
        for s in range(len(self.alphabet)):
            if s == len(self.alphabet) - 1:
                p += self.alphabet[s]
            else:
                p += self.alphabet[s] + ' '
        print(p)

        p = ''
        for s in range(len(self.states)):
            p += self.states[s] + ' '
            for j in range(len(self.alphabet)):
                if j == len(self.alphabet) - 1:
                    p += str(self.emission[s][j])
                else:
                    p = p + str(self.emission[s][j]) + ' '
            if s != len(self.states) - 1:
                p += '\n'

        print(p)


test = Vlearn()
