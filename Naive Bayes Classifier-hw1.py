import sys

datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

#Read data
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0,len(a),1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
    
rows = len(data)
cols = len(data[0])
f.close()  

#Read labels
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
	
#compute means of columns by first initializing means to 1 to avoid division by 0 later on
m0 = []
for j in range(0, cols, 1):
    m0.append(1)
m1 = []
for j in range(0, cols, 1):
    m1.append(1)

#Iteratre over each row of the dataset, check if the label is present or not, if it is present, add the value in that column to corresponding value m0 and m1
for i in range(0, rows, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            m0[j] = m0[j] + data[i][j]
    if(trainlabels.get(i) != None and trainlabels[i] == 1):#
        for j in range(0, cols, 1):
            m1[j] = m1[j] + data[i][j]
            

#Calculate mean of each columns by dividing sum by number of instances in each class
for j in range(0, cols, 1):
    m0[j] = m0[j]/n[0]
    m1[j] = m1[j]/n[1]
	
#compute variance for each column
var0 = []
var1 = []

#initialize variance of each column with 0
for j in range(0, cols, 1):
    var0.append(0)
    var1.append(0)
#Compute squared deviation of the data points from means
for i in range(0, rows, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            var0[j] = var0[j] + (m0[j] - data[i][j])**2
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(0, cols, 1):
            var1[j] = var1[j] + (m1[j] - data[i][j])**2
            
#Computer variance by dividing sum of squared deviations for each class by number of instances minus one
for j in range(0, cols, 1):
    var0[j] = (var0[j]/(n[0]-1))
    var1[j] = (var1[j]/(n[1]-1))   
	
	
#Classify unlabeled data
import math

#Iteratre over each row of the dataset, if the row is unlabeled, initialize two variables d0 and d1 which will store the distance of the data point from means of classes 0 and 1
#Assign data point to the class it is closer to
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        d0 = 0
        d1 = 0
        for j in range(0, cols, 1):
            d0 = d0 + ((m0[j] - data[i][j])**2)/var0[j]
            d1 = d1 + ((m1[j] - data[i][j])**2)/var1[j]
        if(d0<d1):
            print("0", i)
        else:
            print("1", i)   