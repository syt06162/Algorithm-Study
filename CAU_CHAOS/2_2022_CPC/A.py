import sys
input = sys.stdin.readline

N = int(input())

peopleDict = dict()
for _1 in range(N):

    for time in (4,6,4,10):
        lst = list(input().split())
        
        for person in lst:
            if person == "-":
                continue
            elif person in peopleDict:
                peopleDict[person] += time
            else:
                peopleDict[person] = time

minVal = int(1e9)
maxVal = -1
for person in list(peopleDict):
    nowVal = peopleDict[person]
    if nowVal < minVal:
        minVal = nowVal
    elif nowVal > maxVal:
        maxVal = nowVal

if maxVal - minVal <= 12:
    print("Yes")
else:
    print("No")
