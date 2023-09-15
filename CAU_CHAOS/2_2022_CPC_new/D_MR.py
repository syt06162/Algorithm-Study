import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
yongs = list(map(int, input().split()))
rains = list(map(int, input().split()))

parent = [i for i in range(N+1)]
from copy import deepcopy
parent_yongs = [0] + deepcopy(yongs)
parent_rains = [0] + deepcopy(rains)
child_count = [0] + [0 for i in range(N+1)]
hogsu_cnt = 0
for pi in range(1,N+1):
    if parent_yongs[pi] < parent_rains[pi] :
        hogsu_cnt += 1

def find_parent(x):
    if x!=parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    
    global hogsu_cnt

    a = find_parent(a)
    b = find_parent(b)

    before_hong = 0
    before_not = 0
    if parent_yongs[a] < parent_rains[a] :
        before_hong += child_count[a] + 1
    else:
        before_not += child_count[a] + 1
    if parent_yongs[b] < parent_rains[b] :
        before_hong += child_count[b] + 1
    else:
        before_not += child_count[b] + 1
    
    if a>b:
        parent[a] = b
        parent_yongs[b] += parent_yongs[a]
        parent_rains[b] += parent_rains[a]

        child_count[b] += child_count[a] + 1
        child_count[a] = 0

        if parent_yongs[b] < parent_rains[b] :
            hogsu_cnt += before_not
        else:
            hogsu_cnt -= before_hong
    else:
        parent[b] = a
        parent_yongs[a] += parent_yongs[b]
        parent_rains[a] += parent_rains[b]

        child_count[a] += child_count[b] + 1
        child_count[b] = 0

        if parent_yongs[a] < parent_rains[a] :
            hogsu_cnt += before_not
        else:
            hogsu_cnt -= before_hong

for _ in range(M):
    command = input().strip()
    if command=='2':
        print(hogsu_cnt)
    else:
        __, x, y = map(int, command.split())
        # union
        px = find_parent(x)
        py = find_parent(y)
        if px==py: continue
        union(px, py)

