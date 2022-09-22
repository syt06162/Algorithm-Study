import sys
input = sys.stdin.readline

T = int(input())
for _1 in range(T):
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
        a, b = map(int, input().split())
        edges.append((a,b))

    result = 0
    # 크루스칼
    for a,b in edges:
        if find_parent(a) != find_parent(b):
            union(a,b)
            result += 1
    print(result)