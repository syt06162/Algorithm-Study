import sys

N = int(input())
numList = list(map(int, sys.stdin.readline().split()))
ngeList = [-1 for i in range(len(numList))]
stack = []  #<value, index>

index = 0
stack.append(index)
index += 1

while index<len(numList):
    value = numList[index]
    while stack and numList[stack[-1]] < value:
        st_index = stack.pop()
        ngeList[st_index] = value
    stack.append(index)
    index += 1

for i in ngeList:
    print(i, end=" ")