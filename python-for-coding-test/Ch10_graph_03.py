import sys

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(0,N+1)]

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

edges = []
for m in range(M):
    a, b, weight = map(int, sys.stdin.readline().split())
    edges.append((weight, a, b))
edges.sort()

result = []
for edge in edges:
    weight, a, b = edge[0], edge[1], edge[2]
    if find_parent(a) == find_parent(b):
        continue
    else:
        union(a, b)
        result.append(weight)

_max = max(result)
print(sum(result) - _max)