import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

INF = int(1e9)
minVal = INF

finishSet = set() # 조합 절반만 하기 위해
rangeSet = set([i for i in range(N)])
for com in list(combinations([i for i in range(N)], N//2)):
    if com in finishSet:
        continue
    comSet = set(com)
    inSum = 0
    otherSum = 0
    # 포함관계인거 S 값 더하기
    for i in range(N):
        for j in range(0,i):
            if i in comSet and j in comSet:
                inSum += lst[i][j]
                inSum += lst[j][i]
            elif i not in comSet and j not in comSet:
                otherSum += lst[i][j]
                otherSum += lst[j][i]

    minVal = min( minVal, abs(otherSum - inSum))

    finishSet.add(tuple(rangeSet.difference(comSet))) # 이번에 한거 차집합은 할필요 없으니 제거

print(minVal)