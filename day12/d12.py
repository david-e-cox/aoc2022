#!/usr/bin/python3
import collections

# This is the A* search algorithm
# Pretty much copied from wikipedia
def mkPath (cameFrom, current):
    totalPath=[]
    totalPath.append(current)
    while current in cameFrom.keys():
        current = cameFrom[current]
        totalPath.append(current)
    totalPath.reverse()
    return totalPath


def h(goal,loc):
    return (abs(goal[0]-loc[0] + abs(goal[1]-loc[1])))


def aStar (start, goal, heightMap, mapMax):
    offsets = [ (1,0), (-1,0), (0,1), (0,-1)]
    
    openSet  = {start}
    cameFrom = dict()
    
    gScore = collections.defaultdict(lambda:1e9)
    gScore[start]=0;

    fScore = collections.defaultdict(lambda:1e9)
    fScore[start]=h(goal,start)
    
    while len(openSet)>0:
        minValue = 1e9
        for loc in openSet:
            if fScore[loc]<minValue:
                current = loc
                minValue = fScore[loc]


        if current == goal:
            return mkPath(cameFrom,current)

        openSet.remove(current)

        for move in offsets:
            # Next step
            pos = ( move[0]+current[0], move[1]+current[1] )
            # if in bounds
            if pos[0]>0 and pos[0]<=mapMax[0] and pos[1]>0 and pos[1]<=mapMax[1]:
                # if one-step vertically
                if (heightMap[pos]-heightMap[current]) <2:
                    # compute gScore (score is simply "steps", +1)
                    tentative_gScore = gScore[current]+1
                    # if better than existing (or default value) add to path
                    if tentative_gScore < gScore[pos]:
                        cameFrom[pos]=current
                        gScore[pos]=tentative_gScore
                        fScore[pos]=tentative_gScore + h(goal,pos)
                        #Add pos to openSet
                        openSet.add(pos)
           
                        
                        
    
    

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

heightMap=dict()
tryStarts=[]
rCnt=0;cCnt=0

# Process text into a dictionary, with coordinate tuples as keys height as values
# Note goal location and starting point(s) 
for l in lines:
    rCnt+=1
    for c in l:
        cCnt+=1
        heightMap[(rCnt,cCnt)] = ord(c)-ord('a')
        if c=='E':
            goal=(rCnt,cCnt)
            heightMap[goal] = ord('z')-ord('a')
        if c=='S':
            start=(rCnt,cCnt)
            heightMap[start] = 0
        if c=='a':
            tryStarts.append((rCnt,cCnt))
    cCnt=0
    
mapMax=(len(lines), len(l))

# Solve for shortest path, under 1-step height constraint
pathA = aStar(start, goal, heightMap, mapMax)

# Try (blindly...) all possible starting points, retain shortest
minLenB=1e9
for s in tryStarts:
    pathB=aStar(s,goal,heightMap,mapMax)
    if pathB is not None:
        # Note: Steps is path length-1, the start position doesn't count as a step
        if len(pathB)-1<minLenB:
            minLenB=len(pathB)-1
        
print("The answer to Part A is {0:d}".format(len(pathA)-1))
print("The answer to Part B is {0:d}".format(minLenB))


