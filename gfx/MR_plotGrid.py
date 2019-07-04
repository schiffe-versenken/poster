import numpy as np
import matplotlib.pyplot as plt
import pysgpp
import sys

def f(x):
    return x[0]

# arg level is an int
def plotRegularUniformFullGrid(level):
    func = pysgpp.multiFunc(f)
    numDims = 2
    operation = pysgpp.CombigridMultiOperation.createExpUniformBoundaryLinearInterpolation(numDims, func)
    levelManager = operation.getLevelManager()
    levelManager.addRegularLevels(level-1)
    
    P = levelManager.getAllGridPoints()
    plt.plot([0,0,1,1,0],[0,1,1,0,0],'k')
    for i in range(len(P)):
        point=P[i]
        plt.plot(point[0], point[1], 'o',color=(32/255.0,86/255.0,174/255.0), markersize=20)
    plt.axis('equal')
    plt.xlim(xmin=-0.1, xmax=1.1)
    plt.ylim(ymin=-0.1, ymax=1.1)
    plt.axis('off')
        
def plotRegularUniformFullGrids(maxLevel):
    plt.figure()
    #for level in range(1,maxLevel):
    #plt.subplot(1,maxLevel-1,level)
    level = maxLevel
    plotRegularUniformFullGrid(level) 
    path = '/home/rehmemk/SGS_Sync/Konferenzen/2018_03_SimTech/gfx/grid' + str(level) + '.png'
    plt.savefig(path) 
    #plt.show()
        
# arg levelMI is a MultiIndex
def plotRegularUniformSubGrid(levelMI):
    maxLevel = max(levelMI[0], levelMI[1])
    func = pysgpp.multiFunc(f)
    numDims = 2
    operation = pysgpp.CombigridOperation.createExpUniformBoundaryLinearInterpolation(numDims, func)
    levelManager = operation.getLevelManager()
    levelManager.addRegularLevels(maxLevel)
    fullGridEval = operation.getFullGridEval()
    P = fullGridEval.getGridPoints(levelMI)
    plt.plot([0,0,1,1,0],[0,1,1,0,0],'k')
    for i in range(len(P)):
        point=P[i]
        plt.plot(point[0], point[1], 'o', color=(32/255.0,86/255.0,174/255.0), markersize=10)
        
    plt.axis('equal')
    plt.xlim(xmin=-0.1, xmax=1.1)
    plt.ylim(ymin=-0.1, ymax=1.1)
    plt.axis('off')

# arg levelMI is a MultiIndex
def plotRegularUniformSubGridGrey(levelMI):
    maxLevel = max(levelMI[0], levelMI[1])
    func = pysgpp.multiFunc(f)
    numDims = 2
    operation = pysgpp.CombigridOperation.createExpUniformBoundaryLinearInterpolation(numDims, func)
    levelManager = operation.getLevelManager()
    levelManager.addRegularLevels(maxLevel)
    fullGridEval = operation.getFullGridEval()
    P = fullGridEval.getGridPoints(levelMI)
    plt.plot([0,0,1,1,0],[0,1,1,0,0],color=(192/255.0,192/255.0,192/255.0))
    for i in range(len(P)):
        point=P[i]
        plt.plot(point[0], point[1], 'o', color=(192/255.0,192/255.0,192/255.0), markersize=10)
        
    plt.axis('equal')
    plt.xlim(xmin=-0.1, xmax=1.1)
    plt.ylim(ymin=-0.1, ymax=1.1)
    plt.axis('off')    
    
def plotRegularUniformSubGrids():
    plt.figure()
    levels={}
    levelMI = pysgpp.IndexVector(2) # MultiIndex is vector<size_t>
    levelMI[0] = 0;    levelMI[1] = 0;    levels[0] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 1;    levelMI[1] = 0;    levels[1] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 2;    levelMI[1] = 0;    levels[2] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 0;    levelMI[1] = 1;    levels[3] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 1;    levelMI[1] = 1;    levels[4] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 0;    levelMI[1] = 2;    levels[5] = pysgpp.IndexVector(levelMI);

    #grey
    levelMI[0] = 1;    levelMI[1] = 2;    levels[6] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 2;    levelMI[1] = 1;    levels[7] = pysgpp.IndexVector(levelMI);
    levelMI[0] = 2;    levelMI[1] = 2;    levels[8] = pysgpp.IndexVector(levelMI);
    
    plt.subplot(3,3,1)
    plotRegularUniformSubGrid(levels[0])
    plt.subplot(3,3,2)
    plotRegularUniformSubGrid(levels[1])
    plt.subplot(3,3,3)
    plotRegularUniformSubGrid(levels[2])
    plt.subplot(3,3,4)
    plotRegularUniformSubGrid(levels[3])
    plt.subplot(3,3,5)
    plotRegularUniformSubGrid(levels[4])
    plt.subplot(3,3,7)
    plotRegularUniformSubGrid(levels[5])
    plt.text(1.3, 1.05, r'$+$', fontsize=35)
    plt.text(3.15, 2.6, r'$+$', fontsize=35)
    plt.text(1.3, 2.6, r'$-$', fontsize=35)

    plt.subplot(3,3,6)
    plotRegularUniformSubGridGrey(levels[6])
    plt.subplot(3,3,8)
    plotRegularUniformSubGridGrey(levels[7])
    plt.subplot(3,3,9)
    plotRegularUniformSubGridGrey(levels[8])

    path = '/home/rehmemk/SGS_Sync/Konferenzen/2018_03_SimTech/gfx/subgrids3.png'
    plt.savefig(path) 
    #plt.show()

#--------------------------------------------------    
plotRegularUniformFullGrids(3)
#plotRegularUniformSubGrids()







