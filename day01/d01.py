#!/usr/bin/python3

# Read input file
f=open('input.txt');
lines = f.read().splitlines();
f.close()

# Initialize
sTotal=0;
elf=[];

# Loop through input
for cal in lines:
    if len(cal)==0: # If new elf (delimited by empty line)
        elf.append(sTotal);
        sTotal=0; # reset total
        continue;
    # Add elf's snacks into total
    sTotal = sTotal + int(cal);
# sort
elf.sort();

# Solution
print("The answer to part A is {}".format(max(elf)))
print("The answer to part B is {}".format(sum(elf[-3:])))





    
      


