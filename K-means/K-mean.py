import numpy as np
import random
import scipy
from scipy.spatial import distance

#takes path of data.txt file and number of iterations and displays the iteration containing the minimum variation
def import_data(path, itr):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    k = -1
    m = -1
    #dimensions limits
    k_rangeUpper = []
    k_rangeLower = []
    #all points
    points = []
    i = 0
    #extract data into points, set k and m
    for line in lines:
        l = line.split()
        l = [float(f) for f in l]
        if i == 0:
            k = int(l[0])
            m = int(l[1])
        else:
            if i == 1:
                k_rangeLower = l.copy()
                k_rangeUpper = l.copy()
            else:
                for p in range(m):
                    if l[p]>k_rangeUpper[p]:
                        k_rangeUpper[p] = l[p]
                    if l[p]<k_rangeLower[p]:
                        k_rangeLower[p] = l[p]
            points.append(l)
        i += 1


    center, variation = driver(points, k_rangeUpper, k_rangeLower, k, m)
    display(center)
    print("variation: " + str(variation))
    #repeat k-mean algorithm until end
    for v in range(0, itr):
        c, var = driver(points, k_rangeUpper, k_rangeLower, k, m)

        print('run number - ' + str(v))
        if var<variation:
            display(c)
            print("variation: " + str(var))
            center=c.copy()
            variation=var
    print('-------------------')
    display(center)





#takes the points, upper and lower limit for each dimansion, k, and m. returns fixed cluster centers and variation
def driver(points, k_rangeUpper, k_rangeLower, k, m):
    #creating random points
    centers = []
    for i in range(0, k):
        center = []
        for j in range(0, m):
            u = k_rangeUpper[j]
            l = k_rangeLower[j]
            center.append(random.uniform(l, u))
        centers.append(center)

    #finding the clusters with their variations using starting point
    centers, variation = find_clusters(points, centers)
    return (centers, variation)

#main body of algorithm. Takes all the points and returns the fixed center based on random start along with variation
def find_clusters(points, centers):
    diff = True #the centers are different that previous round
    variations = 0 #counter for variations
    while diff:
        variations = 0#reset every new round
        assignee = [[] for i in range(len(centers))]
        #calculate distance to each cluster center for each point and assign to the corresponding index
        #increment variation
        for point in points:
            dist = []
            for center in centers:
                dist.append(scipy.spatial.distance.euclidean(point, center))
            min = np.argmin(dist)
            assignee[min].append(point)
            variations += dist[min]

        diff = False
        i = 0
        #reassign center based on points for each cluster
        for p in assignee:
            if len(p) == 0:
                continue
            newCenter = find_center(p)
            #checks if the center changed
            #will quits only when all centers remain the same - diff remain False
            if newCenter != centers[i]:
                diff = True
                centers[i] = newCenter.copy()
            i+=1
    return (centers , variations)


#finds the mean for all points in a cluster for each dimension
def find_center(points):
    m = len(points[0])
    dimensions = [[]for i in range(m)]
    for i in range(m):
        for point in points:
            dimensions[i].append(point[i])

    center = []
    for d in dimensions:
        center.append(np.mean(d))
    return (center)

#takes the center points and outputs each as a string where each point is rounded to 3rd decimal
def display(points):
    for point in points:
        s = ""
        for i in range(len(point)):
            x = round(point[i], 3)
            x = str(x)
            for j in range(len(x),5):
                x = x+'0'
            if i ==0:
                s += x
            else:
                s = s + " "+ x
        print(s)



import_data('D:\Projects\Bioinformatics\K-means\Data/d7.txt', 70)

