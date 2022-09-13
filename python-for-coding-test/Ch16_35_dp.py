# Ch16_35

import sys
input = sys.stdin.readline

N = int(input())
mot = [False, True] #0:false, 1:true
i = 2
while N>1:
    if (i%2==0 and mot[i//2]==True) or (i%3==0 and mot[i//3]==True) or (i%5==0 and mot[i//5]==True):
        mot.append(True)
        N -= 1
    else:
        mot.append(False)
    i += 1

print(len(mot)-1)