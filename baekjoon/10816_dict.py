import sys

N = int(input())
numLst = list(map(int, sys.stdin.readline().split()))
numDic = dict()
for num in numLst:
    if num in numDic:
        numDic[num] += 1
    else:
        numDic[num] = 1

M = int(input())
findLst = list(map(int, sys.stdin.readline().split()))
for num in findLst:
    if num in numDic:
        print(numDic[num], end=" ")
    else:
        print(-1, end=" ")

