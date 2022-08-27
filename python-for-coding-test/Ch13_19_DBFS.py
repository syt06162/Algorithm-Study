# Ch13_19
# boj 14888
# 핵심: 중복순열을 못쓰니.. 순열을 쓰고, set()

import sys
N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
getsu = list(map(int, sys.stdin.readline().split()))

INF = int(1e9)+10

tools = []
for i in range(getsu[0]):
    tools.append("+")
for i in range(getsu[1]):
    tools.append("-")
for i in range(getsu[2]):
    tools.append("*")
for i in range(getsu[3]):
    tools.append("/")
    
from itertools import permutations
cases = list(set(permutations(tools, N-1)))

minNum = INF
maxNum = -INF
for case in cases:
    nowNum = nums[0]
    for i in range(N-1):
        if case[i]=="+":
            nowNum += nums[i+1]
        elif case[i]=="-":
            nowNum -= nums[i+1]
        elif case[i]=="*":
            nowNum *= nums[i+1]
        elif case[i]=="/":
            if nowNum<0:
                nowNum = -(-nowNum // nums[i+1])
            else:
                nowNum //= nums[i+1]
        
    minNum = min(minNum, nowNum)
    maxNum = max(maxNum, nowNum)

print(maxNum)
print(minNum)
