import sys

N = int(input())
numList = list(map(int, sys.stdin.readline().split()))
ngeList = [-1 for _ in range(len(numList))]
stack = []  #<index>

for index in range(N):
    value = numList[index]
    while stack and numList[stack[-1]] < value:
        st_index = stack.pop()
        ngeList[st_index] = value
    stack.append(index)

for i in ngeList:
    print(i, end=" ")