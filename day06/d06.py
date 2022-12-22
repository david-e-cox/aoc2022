#!/usr/bin/python3

def findMarker(stream,nUnique):
    buffer=[]
    for i in range(len(stream)):
        if len(buffer)<nUnique:
            buffer.append(stream[i])
        else:
            buffer[i%nUnique]=stream[i]

        if len(set(buffer))==nUnique:
            ndx=i+1
            break
    return ndx

    

# Read input file
f=open('input.txt');
stream = f.readline().strip()
f.close()

print("The answer to Part A is {0:d}".format(findMarker(stream,4)))
print("The answer to Part B is {0:d}".format(findMarker(stream,14)))


