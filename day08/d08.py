#!/usr/bin/python3
import numpy as np

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Initialize numpy arrays
nRows = len(lines)
nCols = len(lines[0])
forestA   = np.zeros( [nRows+2,nCols+2], dtype='int')
forestB   = np.zeros( [nRows,nCols],dtype='int')
visible   = np.ones(  [nRows+2,nCols+2],dtype='int')
sightMetric = np.zeros( [nRows,nCols], dtype='int')

# Populate from input file
for i in range(nRows):
    for j in range(nCols):
        forestA[i+1,j+1] = int(lines[i][j])
        forestB[i,j] = int(lines[i][j])
        
# PART A - oversize forest with visible edges
for i in range(2,forestA.shape[0]-2):
    for j in range(2,forestA.shape[1]-2):
        tree = forestA[i,j]
        # Mark trees as invisible if there are taller trees all around
        if np.max(forestA[:i,j])>=tree and np.max(forestA[i+1:,j])>=tree and np.max(forestA[i,:j])>=tree and np.max(forestA[i,j+1:])>=tree:
            visible[i,j]=0
sumInvisible = np.prod(visible.shape) - np.count_nonzero(visible)
nTrees = nRows*nCols

# PART B
#  Key here is handling see-to-the-edge cases.  Below the have empty view array
for i in range(1,forestB.shape[0]-1):
    for j in range(1,forestB.shape[1]-1):
        tree=forestB[i,j]

        view = np.where(forestB[:i,j]  - tree >= 0)[0]
        if len(view)>0:
            upDist =  i-np.max(view)
        else:
            upDist=i

        view = np.where(forestB[i+1:,j]  - tree >= 0)[0]
        if len(view)>0:
            dnDist =  np.min(view)+1
        else:
            dnDist=nRows-(i+1)

        view = np.where(forestB[i,:j]  - tree >= 0)[0]
        if len(view)>0:
            lfDist =  j-np.max(view)
        else:
            lfDist=j
        
        view = np.where(forestB[i,j+1:]  - tree >= 0)[0]
        if len(view)>0:
            rtDist =  np.min(view)+1
        else:
            rtDist=nCols-(j+1)
    
        sightMetric[i,j]=upDist*dnDist*lfDist*rtDist
        
print("The answer to Part A is {}".format(nTrees - sumInvisible))
print("The answer to Part B is {}".format(np.max(sightMetric)))


