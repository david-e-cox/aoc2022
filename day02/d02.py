#!/usr/bin/python3

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# ----------- Part A ---------------    
# Game Rules, dictionary keys are my shape
ties  = {'X':'A', 'Y':'B', 'Z':'C'};
beats = {'X':'C', 'Y':'A', 'Z':'B'};

# Augmentation points
points= {'X':1, 'Y':2, 'Z':3};

# Play rounds, compute score
scoreA=0;
for match in lines:
    if ties[match[2]]==match[0]:     # If my play ties
        scoreA+=3;
    elif beats[match[2]]==match[0]:  # My play wins
        scoreA+=6;

    # Augment score based on shape played
    scoreA += points[match[2]];


# ----------- Part B ---------------    
# Game Rules, dictionary keys are opponents shape
loseTo      = {'A':'C', 'B':'A', 'C':'B'}
winAgainst  = {'A':'B', 'B':'C', 'C':'A'}
# Augmentation points
points      = {'A':1,   'B':2,   'C':3}

# Play rounds, compute score
scoreB=0;
for match in lines:
    if match[2]=='X':
        myShape = loseTo[match[0]]
    elif match[2]=='Y':
        myShape = match[0]
        scoreB += 3
    else:
        myShape = winAgainst[match[0]]
        scoreB += 6

    # Augment score based on shape played
    scoreB += points[myShape]
        
# Solution
print("The answer to part A is {}".format(scoreA))
print("The answer to part B is {}".format(scoreB))





    
      


