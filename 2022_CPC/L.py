import sys
sys.setrecursionlimit(100001)
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
yong = list(map(int, input().split()))
rain = list(map(int, input().split()))

parent = [i for i in range(N)]
yongSum = deepcopy(yong)
rainSum = deepcopy(rain)
childSum = [1 for i in range(N)]

# 현재 넘치는(홍수) 것의 개수 구하기
hongsuSum = 0
for i in range(N):
    if yongSum[i] < rainSum[i]:
        hongsuSum += 1

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a,b):
    global hongsuSum

    a = find_parent(a)
    b = find_parent(b)
    if a==b:
        # 같은 경우는 union 해주면 오류남
        return
    elif a>b:
        parent[a] = b
        # 기존 홍수개수 다 지우고
        if yongSum[a] < rainSum[a]:
            hongsuSum -= childSum[a]
        if yongSum[b] < rainSum[b]:
            hongsuSum -= childSum[b]

        # 다시 계산 후
        yongSum[b] += yongSum[a]
        rainSum[b] += rainSum[a]
        childSum[b] += childSum[a]

        # 다시 홍수개수 업데이트
        if yongSum[b] < rainSum[b]:
            hongsuSum += childSum[b]
    else:
        parent[b] = a
        # 기존 홍수개수 다 지우고
        if yongSum[a] < rainSum[a]:
            hongsuSum -= childSum[a]
        if yongSum[b] < rainSum[b]:
            hongsuSum -= childSum[b]

        # 다시 계산 후
        yongSum[a] += yongSum[b]
        rainSum[a] += rainSum[b]
        childSum[a] += childSum[b]

        # 다시 홍수개수 업데이트
        if yongSum[a] < rainSum[a]:
            hongsuSum += childSum[a]


# 쿼리 받기
for _1 in range(M):
    command = input().strip()
    if command[0] == '2':
        print(hongsuSum)
    else:
        temp, a, b = map(int, command.split())
        union_parent(a-1,b-1)
