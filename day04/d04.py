#!/usr/bin/python3

def contains(rangeA,rangeB):
    return( (rangeA[0] <= rangeB[0]) & (rangeA[1] >= rangeB[1]) )

def overlaps(rangeA,rangeB):
    return( (rangeA[0] <= rangeB[1]) & (rangeA[1] >= rangeB[0]) )
    
# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

Ncontain=0
Noverlap=0
for section in lines:
    sectionAB =  section.split(',')
    A  = [int(x) for x in sectionAB[0].split('-')]
    B  = [int(x) for x in sectionAB[1].split('-')]
    if (contains(A,B) | contains(B,A)):
        Ncontain+=1
    if (overlaps(A,B) | overlaps(B,A)):
        Noverlap+=1
    
            
print("The answer to Part A is {0:d}".format(Ncontain))
print("The answer to Part B is {0:d}".format(Noverlap))


