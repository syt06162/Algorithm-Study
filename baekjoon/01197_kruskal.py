import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find_parent(a):
    if a!=parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

edges = []
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a,b))
edges.sort()

result = 0
# 크루스칼
for cost, a,b in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        result += cost
print(result)