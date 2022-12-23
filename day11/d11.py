#!/usr/bin/python3
import collections

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()


# Initial a zoo array with monkey dictionaries
#    A queue to hold items
#    Lambda functions for operate and test
#    A target touple, and an inspection counter
zoo = [{'items':collections.deque([]),
        'oper': lambda x:x+0,
        'test': lambda x:x==0,
        'target':(0,0),
        'inspect':0} for _ in range(8)]


# Parsing is messy on this one, processing the input with grep/emacs:

## Example
#items = [ [79,98],
#          [54,65,75,74],
#          [79,60,97],
#          [74] ]
#
#for i in range(len(items)):
#    items[i].reverse()
#    zoo[i]['items']=collections.deque(items[i])
#
#zoo[0]['oper']  = lambda x:x*19
#zoo[0]['test']  = lambda x:x%23==0
#zoo[0]['target']= (2,3)
#
#zoo[1]['oper']  = lambda x:x+6
#zoo[1]['test']  = lambda x:x%19==0
#zoo[1]['target']= (2,0)
#
#zoo[2]['oper']  = lambda x:x*x
#zoo[2]['test']  = lambda x:x%13==0
#zoo[2]['target']= (1,3)
#
#zoo[3]['oper']  = lambda x:x+3
#zoo[3]['test']  = lambda x:x%17==0
#zoo[3]['target']= (0,1)
#

## Manually processed input.txt file
items = [ [63, 57],
          [82, 66, 87, 78, 77, 92, 83],
          [97, 53, 53, 85, 58, 54],
          [50],
          [64, 69, 52, 65, 73],
          [57, 91, 65],
          [67, 91, 84, 78, 60, 69, 99, 83],
          [58, 78, 69, 65] ]
 
for i in range(len(items)):
    items[i].reverse()
    zoo[i]['items']=collections.deque(items[i])
 
zoo[0]['oper'] = lambda x:x * 11
zoo[1]['oper'] = lambda x:x + 1
zoo[2]['oper'] = lambda x:x * 7
zoo[3]['oper'] = lambda x:x + 3
zoo[4]['oper'] = lambda x:x + 6
zoo[5]['oper'] = lambda x:x + 5
zoo[6]['oper'] = lambda x:x * x
zoo[7]['oper'] = lambda x:x + 7
 
zoo[0]['test'] = lambda x:x%7 ==0
zoo[1]['test'] = lambda x:x%11==0
zoo[2]['test'] = lambda x:x%13==0
zoo[3]['test'] = lambda x:x%3 ==0
zoo[4]['test'] = lambda x:x%17==0
zoo[5]['test'] = lambda x:x%2 ==0
zoo[6]['test'] = lambda x:x%5 ==0
zoo[7]['test'] = lambda x:x%19==0

zoo[0]['target'] = (6,2)
zoo[1]['target'] = (5,0)
zoo[2]['target'] = (4,3)
zoo[3]['target'] = (1,7)
zoo[4]['target'] = (3,7)
zoo[5]['target'] = (0,6)
zoo[6]['target'] = (2,4)
zoo[7]['target'] = (5,1)




#Initialize
#wrapLvl=23*19*13*17 # Example
wrapLvl=7*11*13*3*17*2*5*19
partA = False
done = False

round=0
while not done:
    round+=1;
    # For each monkey
    for m in zoo:
        # For each item they hold
        for _ in range(len(m['items'])):
            worry = m['items'].pop()
            # Score counter, based on inspections
            m['inspect']+=1
            # Increment worry
            # (part B requires modulo operator with proper warp around level)
            worry = m['oper'](worry)
            if partA:
                worry = int(float(worry)/3.0)
            else:
                worry=worry%wrapLvl
            # Figure out who to throw it to
            if m['test'](worry):
                tgt=m['target'][0]
            else:
                tgt=m['target'][1]
            # Toss item
            zoo[tgt]['items'].appendleft(worry)

    #if (round in [20,1000,2000,3000,10000]):
    #    print()
    #    for m in zoo:
    #        print("Monkey Inpsection Count: {}".format(m['inspect']))

    if (partA):
        if (round==20):
            done=True
    else:
        if (round==10000):
            done=True

scores=[]        
for m in zoo:
    scores.append(m['inspect'])
scores.sort()
# Answer is product of highest two scores
if (partA):
    print("The answer to Part A is {0:d}".format(scores[-2]*scores[-1]))
else:
    print("The answer to Part B is {0:d}".format(scores[-2]*scores[-1]))


