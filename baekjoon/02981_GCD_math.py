import sys
import math

N = int(input())
numLst = []
for i in range(N):
    numLst.append(int(sys.stdin.readline()))
numLst.sort()

subLst = [] #입력받은 정수들의 차이를 저장하는 배열
for i in range(N-1):
    subLst.append(numLst[i+1]-numLst[i])

GCDval = math.gcd(*subLst) #차이들의 최대공약수 구하기

def getYaksu(num): #최대공약수의 모든 약수 구하기 (1제외)
    sosulst = []
    templst = []
    i = 1
    sq = int(num**(1/2))
    for i in range(1, sq+1):
        if num%i == 0:
            sosulst.append(i)
            templst.append(num//i)

    if templst[-1] == sosulst[-1]:
        templst.pop()

    while templst:
        sosulst.append(templst.pop())

    return sosulst[1:]

result = getYaksu(GCDval)

print(*result)