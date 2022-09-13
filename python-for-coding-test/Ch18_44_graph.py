# Ch18_44

import sys
input = sys.stdin.readline
N = int(input())

xList = []
yList = []
zList = []
for i in range(N):
    x,y,z = map(int, input().split())
    xList.append((x, i)) 
    yList.append((y, i)) 
    zList.append((z, i)) 
xList.sort()
yList.sort()
zList.sort()

# edges 후보 구하기
edges = []
for i in range(1,N):
    cost = xList[i][0] - xList[i-1][0]
    edges.append((cost, xList[i][1], xList[i-1][1]))

    cost = yList[i][0] - yList[i-1][0]
    edges.append((cost, yList[i][1], yList[i-1][1]))
    
    cost = zList[i][0] - zList[i-1][0]
    edges.append((cost, zList[i][1], zList[i-1][1]))
edges.sort()

# 서로소 집합 함수
parent = [i for i in range(N+1)] # 0번지 사용 x

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 크루스칼
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union(a,b)
        result += cost
print(result)
