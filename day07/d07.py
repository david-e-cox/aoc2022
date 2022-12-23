#!/usr/bin/python3
from collections import defaultdict

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Initialize
cmdMode=False
fileMap = dict()
totalSize = defaultdict(lambda:0)
dirSet  = set()

# Initial directory, prepopulate
# It's there, but we don't down "cd" to it
dirSet.add('/')

# Parse input file
for line in lines:
    # cmdMode determines if this line of the file is a command or the
    # return from a previous command
    # commands (cd, ls) get responed to
    # Really just by updating the path-to-working directory (pwd)
    if line.startswith("$ cd"):
        cmdMode=True
        cmd = line.split(' ');
        if cmd[2]=='..':
            ndx=pwd.rfind('/')
            pwd=pwd[:max(ndx,1)]

        elif cmd[2]=='/':
            pwd ='/'
        else:
            if pwd[-1]!='/':
                pwd+="/"
            pwd+= cmd[2]
            dirSet.add(pwd)


    if line.startswith("$ ls"):
        # Switch to processing line
        cmdMode=False
        continue
        
    if (not cmdMode):
        if line.startswith("dir"):
            #do nothing
            continue
        else:
            info=line.split(' ')
            key =  pwd;
            # Ensure delimiter between folders/files
            if key[-1]!='/':
                key+="/"
            # The fileMap dictonary stores the size info, with a full-path as the key
            fileMap[key+info[1]] = int(info[0])


# Create the database, finding sizes for every directory discovered            
for folder in dirSet:
    for path in fileMap.keys():
        if path.startswith(folder):
            totalSize[folder]+=fileMap[path]
    
# Print for debugging
#for folder in totalSize.keys():
#    print("Folder {0:10}: {1:d} bytes".format(folder,totalSize[folder]))
    
# Make a list of tuples from dictionary data, to allow sorting
sumBytes=0
for folder in totalSize.keys():
    if totalSize[folder]<100000:
        sumBytes+=totalSize[folder]

# Sort by size
dirList=[];
for folder in totalSize.keys():
    dirList.append( (totalSize[folder],folder))
dirList =sorted(dirList)

#search for smallest folder which has the required space
requiredSize = 30000000-(70000000 - totalSize['/'])

for x in dirList:
    if (x[0] > requiredSize):
        solSize =(x[0])
        break

#Print solutions    
print("The answer to Part A is {}".format(sumBytes))
print("The answer to Part B is {}".format(solSize))


