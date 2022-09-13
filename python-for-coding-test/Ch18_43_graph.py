# Ch18_43

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
costSum = 0
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    costSum += cost
edges.sort()

# parent와 서로소 집합 함수
parent = [i for i in range(N)]

def find_parent(a):
    if a!=parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a,b):
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

print(costSum - result)


'''
7 11
0 1 7 
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''