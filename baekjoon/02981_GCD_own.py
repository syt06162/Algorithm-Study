import sys

N = int(input())
numLst = []
for i in range(N):
    numLst.append(int(sys.stdin.readline()))
numLst.sort() 

subLst = [] #입력받은 정수 정렬하고, 차이를 저장.
for i in range(N-1):
    subLst.append(numLst[i+1]-numLst[i])

def getGCD(*integers): #subLst 요소들의 최대공약수 구하기
    bound = min(integers)
    while bound > 0: 
        idx = 0
        while idx < len(integers):
            if integers[idx] % bound != 0:
                break
            idx += 1
        else:
            return bound
        bound -= 1
    return -1

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

GCD = getGCD(*subLst)
result = getYaksu(GCD)

print(*result)