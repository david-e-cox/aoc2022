#!/usr/bin/python3
import math
# Read input file

def follow(head,tail):
    dx = head[0]-tail[0]
    dy = head[1]-tail[1]

    # Adjacent, no action
    if abs(dx)<2 and abs(dy)<2:
        return tail

    # Up or down, follow
    if dx==0:
        if dy>0:
            tail[1]+=1
        else:
            tail[1]-=1
        return tail

    # Left or right, follow
    if dy==0:
        if dx>0:
            tail[0]+=1
        else:
            tail[0]-=1
        return tail

    # On a corner, follow along diagonal
    tail[0]+=math.copysign(1,dx)
    tail[1]+=math.copysign(1,dy)
    return tail



def printMap(headPos,tailPos):
    for y in range(-5,5):
        for x in range(-10,10):
            marked=False
            if headPos[0]==x and headPos[1]==y:
                print('H',end='')
                marked=True

            if tailPos[0]==x and tailPos[1]==y and not marked:
                print('T',end='')
                marked=True

            if x==0 and y==0 and not marked:
                print('s',end='')
                marked=True
            
            if not marked:
                print('.',end='')
        print()
    print()

    
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Initialize
headPos=[0,0]
tailPos=[0,0]
moveDir = {'U':(0,1), 'D':(0,-1), 'L':(-1,0),'R':(1,0)}
tailTracks =set()
tail9Tracks=set()
#printMap(headPos,tailPos)

#Part A
for move in lines:
    direction,dist=move.split(' ')
    for cnt in range(int(dist)):
        headPos[0]+=moveDir[direction][0]
        headPos[1]+=moveDir[direction][1]
        #printMap(headPos,tailPos)
        tailPos = follow(headPos,tailPos)
        #printMap(headPos,tailPos)
        tailTracks.add((tailPos[0],tailPos[1]))

# Part B
rope=[ [0,0] for _ in range(10)]
for move in lines:
    direction,dist=move.split(' ')
    for cnt in range(int(dist)):
        rope[0][0] += moveDir[direction][0]
        rope[0][1] += moveDir[direction][1] 
        for i in range(1,10):
            rope[i] = follow(rope[i-1],rope[i])
        tail9Tracks.add((rope[9][0],rope[9][1]))


print("The answer to Part A is {0:d}".format(len(tailTracks)))
print("The answer to Part B is {0:d}".format(len(tail9Tracks)))


