import numpy as np
import matplotlib.pyplot as plt
import pysgpp

def getUniformPoints(level):
    if level == 0:
        points=[0.5]
    else:
        points=np.linspace(0,1,2**level+1)
    return points

def getIndices(level):
    if level == 0:
        indices = [0]
    else:
        indices=range(0,2**level+1)
    return indices 

def Bsplinevalues(X,degree,index,points):
    B=[0]*len(X)
    for i,x in enumerate(X):
        temp = pysgpp.expUniformNakBspline(x, degree, index, points)
        if temp>0.0:
            B[i] = temp
        else:
            B[i]='nan' 
    return B

def plotBspline(degree, level, index):
    points=getUniformPoints(level)
    X=np.linspace(0,1,1000)
    if (degree == 3 and level > 1) or (degree == 5 and level >2): 
        np.divide(X,1.0/(2**level))
        np.subtract(X,index)
    B=Bsplinevalues(X,degree,index,points)
    
    plt.plot(X,B,linewidth=1.5,color=(32/255.0,86/255.0,174/255.0))
    #ax = plt.axes()
    #ax.get_xaxis().tick_bottom()           # remove top ticks
    #ax.axes.get_yaxis().set_visible(False) # turn y axis off
    
def plotWholeLevel(level,degree):
    indices = getIndices(level)
    for index in indices:
        plotBspline(degree,level,index)            
    points = getUniformPoints(level)
    plt.xticks(points)
    plt.yticks([])


#-----------------------------------------------------------------------

plt.figure(figsize=(10,3))
ax=plt.gca()
degree = 3
plotWholeLevel(3, degree)
x = [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1]
labels = ['$x_0$', '$x_1$', '$x_2$', '$x_3$','$x_4$','$x_5$','$x_6$','$x_7$','$x_8$']
plt.xticks(x, labels,fontsize=20)

activepoints = [0,  0.25, 0.375, 0.5, 0.625, 0.75, 1]
plt.plot(activepoints,[0]*len(activepoints),'o',markersize=12,color=(32/255.0,86/255.0,174/255.0))
inactivepoints = [0.125,0.875]
plt.plot(inactivepoints,[0]*len(inactivepoints),'o',markersize=12,color=(192/255.0,192/255.0,192/255.0))
plt.xlim(-0.02,1.02)
plt.ylim(-0.03,0.75)
plt.axis('off')
ax.axes.get_yaxis().set_visible(False)


plt.tight_layout()
#plt.show()
path = '/home/rehmemk/SGS_Sync/Konferenzen/2018_03_SimTech/gfx/nakBsplineBasis_33.png' 
plt.savefig(path)
