import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
letters = list(sys.stdin.readline().split())
letters.sort()

moum = ['a', 'e', 'i', 'o', 'u']

lst = list(combinations(letters, L))
for word in lst:
    moumNum = 0
    for l in word:
        if l in moum:
            moumNum += 1

    if moumNum>=1 and L-moumNum >=2:
        print(*word, sep="")

# 4 6
# a t c i s w