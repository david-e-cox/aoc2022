#!/usr/bin/python3
import math
# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

cpu = {'cycle':0,'sigLvl':0,'reg':1,'screen':[' ' for _ in range(240)]}

def drawPix(screen):
    rowOffset = int(math.floor(float(cpu['cycle'])/40.0)*40)
    if abs((cpu['cycle']-1)%40-cpu['reg'])<2:
        screen[(cpu['cycle']-1)%40 + rowOffset] = '#'
    return screen

def advCycle(cpu):
    lookFor=[20, 60, 100, 140, 180, 220]
    cpu['cycle']+=1
    cpu['screen']=drawPix(cpu['screen'])
    if cpu['cycle'] in lookFor:
        #print("At {} have siglevel of {}, regVal={}".format(cpu['cycle'],cpu['reg']*cpu['cycle'],cpu['reg']))
        cpu['sigLvl'] += cpu['cycle']*cpu['reg']
    return cpu

done = False

lineCnt=0;

while not done:
    if lines[lineCnt]=='noop':
        cmd='noop'
    else:
        cmd,param=lines[lineCnt].split(' ')

    if cmd=='noop':
        cpu=advCycle(cpu)

    elif cmd=='addx':
        cpu=advCycle(cpu)
        cpu=advCycle(cpu)
        cpu['reg']+= int(param)


    lineCnt+=1;
    if lineCnt>=len(lines):
        done=True


print("The answer to Part A is {0:d}".format(cpu['sigLvl']))

print("The answer to Part B is:")
for i in range(240):
    cnt=i%40
    if cnt==0:
        print()
    print(cpu['screen'][i],end='')
print()




