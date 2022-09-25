import sys
input = sys.stdin.readline

# 1. 개인 풀이 - 좌우 비교 result, 자기값은 distance
# 2. 검색해본 풀이 - 아무데서나 bfs해서 최장 찾고, 거기서 다시 bfs로 최장 찾으면 그 것이 거리

N = int(input())
graph = [[] for i in range(N+1)] #0x

for i in range(N):
    lst = list(map(int, input().split()))
    now = lst[0]
    idx = 1
    while True:
        if lst[idx] == -1:
            break
        graph[now].append((lst[idx], lst[idx+1]))
        idx += 2

distance = [-1 for i in range(N+1)]
# 아무 점에서 dfs로 리프노드까지 순회하고, 
# 리프노드면 dis=0, 그외는 dis[child]+거리 의 두 최대값 합

result = -1
def dfs(now, par):
    if len(graph[now])==1 and graph[now][0][0] == par:
        distance[now] = 0
        return
    
    global result
    costList = []
    for child, cost in graph[now]:
        if child == par:
            continue
        dfs(child, now)
        costList.append(distance[child] + cost)
        
    # 길이가 1이면 그것, 그외면 max1+max2
    distance[now] = max(costList)
    if len(costList) == 1:
        result = max(result, costList[0])
    else:
        max1 = max(costList)
        costList.remove(max1)
        max2 = max(costList)
        result = max(max1 + max2, result)

dfs(1,-1)
print(result)
        