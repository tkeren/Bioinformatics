import plotly.plotly as py
import plotly
#plotly.tools.set_credentials_file(username='username', api_key='****************')
import plotly.graph_objs as go
import numpy as np
import random
import scipy
from scipy.spatial import distance
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#takes path of data.txt file and returns a vector of points as well as K
def import_data(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    k = -1
    m = -1
    points = []
    #extract data into points
    for i, line in enumerate(lines):
        l = line.split()
        l = [float(f) for f in l]
        if i == 0:
            k = int(l[0])
            m = int(l[1])
        else:
            points.append(l)

    return(points, k)


#given the data set, k-value, and n number of iterations(deafult 6) ->
#apply K-mean clustering n times saving the one with smallest variation
#for finding optimal k -> returns center points, W, and B for CH index
#else returns set of center points and k sets of points each set contains points of each cluster
def driver(points, k, iterations=6, optimalK=False):
    center, variation, assignee = Kmean(points, k)
    #repeat k-mean algorithm until end
    for v in range(0, iterations):
        c, var, assigneetemp = Kmean(points, k)
        print('run #' + str(v))

        if var<variation:
            #display(c)
            center=c.copy()
            variation=var
            assignee=assigneetemp.copy()
    print('-------------------')
    if not optimalK:
        return(center, assignee)
    else:
        B=0
        for c in range(len(center)):
            for c2 in range(len(center)):
                B+=distance.euclidean(center[c], center[c2])
        return (center, variation, B)







#main body of algorithm. Takes all the points and returns the fixed center based on random start along with variation
def Kmean(points, k):
    # selecting K random points
    centers = random.sample(points, k)
    # finding the clusters with their variations using starting point
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
        #plotcluster(points, k, assignee)
        #reassign center based on points for each cluster
        for i, p in enumerate(assignee):
            if len(p) == 0:
                continue
            newCenter = find_center(p)
            #checks if the center changed
            #will quits only when all centers remain the same - diff remain False
            if newCenter != centers[i]:
                diff = True
                centers[i] = newCenter.copy()

    return (centers , variations, assignee)


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


#Uses CH index to find optimal K
#incomplete
def optimalK(points, low, high):
    centers = []
    n = len(points)
    CH = []
    for i in range(low,high):
        center, var, B = driver(points,i, optimalK=True)
        CH.append((var/(i-1))/(B/(n-i)))
        centers.append(center)
    ks = [i for i in range(low,high)]

    plt.plot(ks, CH)
    plt.show()

#visualizations of the cluster (only 3d)
def plotcluster(points, k):#, asignee):
    center, asignee = driver(points, k)
    color = ['red', 'blue', 'green', 'yellow', 'black', 'pink']
    fig = plt.figure()
    ax = fig.add_subplot(111)#, projection='3d')
    for i, point in enumerate(asignee):
        a = []
        b = []
        c = []
        for p in point:
            a.append(p[0])
            b.append(p[1])
            #c.append(p[2])
        ax.scatter(a, b, color=color[i])
    plt.show()


def ThreeDplotting(points, k):
    center, asignee = driver(points, k)
    traces = []
    color = ['red', 'blue', 'green', 'yellow', 'black', 'pink']
    for i, point in enumerate(asignee):
        a = []
        b = []
        c = []
        for p in point:
            a.append(p[0])
            b.append(p[1])
            c.append(p[2])
        trace = go.Scatter3d(
            x=a,
            y=b,
            z=c,
            mode='markers',
            marker=dict(
                size=8,
                color=color[i],  # set color to an array/list of desired values
                colorscale='Viridis',  # choose a colorscale
                opacity=0.8
            )
        )
        traces.append(trace)
    data = traces
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='3d-scatter-colorscale')


points, k = import_data('Data/d3.txt')
#optimalK(points,2,8)
plotcluster(points, 6)
#driver(points, 2, iterations=4)
#ThreeDplotting(points, k)


