#!/usr/bin/python3
import collections
import copy
import re

def printStacks(stacks):
    for cnt in range(len(stacks)):
        tmp = stacks[cnt]
        print("={}=  ".format(cnt+1),end='')
        for i in range(len(tmp)):
            print(" [{}]".format(tmp[i]),end='')
        print()

        
# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()


# Initialize
onStack  = True;
quantity = [];
moveFrom = [];
moveTo   = [];
# Using a list of double-ended queues here to represent stacks of boxes
# The pop()/append() operations remove/add elements cleanly for "box moving"
stacksA = [ collections.deque([]) for _ in range(9)] 

# Process input file
# First bit is the starting stack of boxes
for row in lines:
    if len(row)>1:
        if row[1]=='1':
            break  # Once we have the stacks, exit this loop

        rowOfBoxes=[]
        for i in range(len(stacksA)):
            rowOfBoxes.append(row[i*4+1])  # Indexing to letters, fragile ;(

        colNdx=0
        for box in rowOfBoxes:
            if (box!=' '):
                stacksA[colNdx].appendleft(box)  # Using appendleft.  Nominally a FIFO buffer, but filling here top first
            colNdx+=1


# Second bit is the move instructions        
for row in lines:
    if len(row)>4:
        if row[:4]=="move":
            ins = re.split("move (\d+) from (\d+) to (\d+)", row)
            quantity.append(int(ins[1]))
            moveFrom.append(int(ins[2])-1)
            moveTo.append(  int(ins[3])-1)
        

# Echo setup to screen            
#print(); printStacks(stacksA)

# Need a deep copy of our stack list to use in partB
stacksB = copy.deepcopy(stacksA)

#---------------- Part A ---------------------
# process moves with pop/append on FIFO queue to move boxes
for i in range(len(moveTo)):
    for _ in range(quantity[i]):
        frm  = moveFrom[i]
        to   = moveTo[i]
        stacksA[to].append(stacksA[frm].pop())
    # Echo boxes at each iteration
    #print(); printStacks(stacksA)

# Compute solution, pop the top of each stack    
partA=''
for i in range(len(stacksA)):
    partA+=stacksA[i].pop()


#---------------- Part B ---------------------
# process moves with pop/append on FIFO queue to move boxes
for i in range(len(moveTo)):
    boxGrp=[]
    for _ in range(quantity[i]):
        frm  = moveFrom[i]
        to   = moveTo[i]
        boxGrp.append(stacksB[frm].pop())
    boxGrp.reverse()
    for box in boxGrp:
        stacksB[to].append(box)

# Compute solution, pop the top of each stack    
partB=''
for i in range(len(stacksB)):
    partB+=stacksB[i].pop()

# Print Answers    
print("The answer to Part A is {}".format(partA))
print("The answer to Part B is {}".format(partB))


