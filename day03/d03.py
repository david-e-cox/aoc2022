#!/usr/bin/python3
def scoreItems(l):
    score=0
    for item in l:
        # Using ASCII character values (plus offset) to computer item score
        if item.islower():
            score += ord(item)-96   #'a' is ASCII 97
        else:
            score += ord(item)-64+26 # 'A' is ASCII 65
    return(score)


# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Initialize
inBoth    = []  # List of all items in both compartments
triCommon = []  # List of all items common to a 3-set of rucksacks
sackSets  = [set(), set(), set()];
sackCnt   = 0

for rsack in lines:   # Each rucksack
    #Initialize
    compA = set()
    compB = set()
    itemCnt = 0

    # Loop through rucksack, make sets for compartment A and B
    for item in rsack:
        if itemCnt< (len(rsack)/2):
            compA.add(item)
        else:
            compB.add(item)
        # Increment item count
        itemCnt+=1

    # Use set intersection find common item to both compartments
    inBoth.append( (compA & compB).pop() )

    # Track 3 sequential sacks in sets, with items from both compartments
    sackSets[sackCnt] = compA | compB

    # When the third sack is defined, look for intersection of all 3
    if (sackCnt)==2:
        triCommon.append( (sackSets[0] & sackSets[1] & sackSets[2]).pop() )

    # Increment sack count, for identifying 3 in sequence
    sackCnt = (sackCnt+1)%3
    
print("The answer to Part A is {0:d}".format(scoreItems(inBoth)))
print("The answer to Part B is {0:d}".format(scoreItems(triCommon)))



