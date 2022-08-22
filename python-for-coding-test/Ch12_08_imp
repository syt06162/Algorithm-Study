# Ch12_08

import sys
DIGIT = set(str(i) for i in range(10))

st = input()

letters = []
numSum = 0
for c in st:
    if c in DIGIT:
        numSum += int(c)
    else:
        letters.append(c)
letters.sort()

print(*letters, str(numSum), sep="")
    
