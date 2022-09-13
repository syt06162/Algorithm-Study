# Ch18_42

import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
planes = []
for i in range(P):
    planes.append(int(input()))

gateParent = [i for i in range(0,G+1)] # 0번지는 사용안함

def find_parent(a):
    if gateParent[a] != a:
        gateParent[a] = find_parent(gateParent[a])
    return gateParent[a]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        gateParent[b] = a
    else:
        gateParent[a] = b

# 각각 비행기 gi에 대해, i번째 gate의 parent에 도킹. 
# 도킹 이후 i-1 번째 gate와 유니온.
result = 0
for plane in planes:
    nowDock = find_parent(plane) # union find 알고리즘의 핵심 함정 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 여기를 find_parent(plane) 이 아닌 parent[plane] 으로 할 경우 올바른 정렬이 안 됨.
    # 함수 구현 외의 부분에서는 parent[a] 로 사용 X, 반드시 find_parent(a) 로 사용 O !! (그래야 그때 정렬과 동시에 find)

    # 부모가 0인 경우는 도킹 자리가 없는것
    if nowDock != 0:
        result += 1
        union(nowDock, nowDock-1)
    else:
        break
print(result)
# print(gateParent)