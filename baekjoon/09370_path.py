import sys
import heapq
input = sys.stdin.readline

# 다익스트라
# 꿀팀 - gh 간선만 0.01 빼기

T = int(input())
for _ in range(T):
    n , m , t = map(int, input().split())
    s , g , h = map(int, input().split())
    
    graph = [[] for i in range(n+1)] # 0번지 x
    for i in range(m):
        a, b, cost = map(int, input().split())
        if a in [g,h] and b in [g,h]:
            graph[a].append((b,cost-0.01))
            graph[b].append((a,cost-0.01))
        else:
            graph[a].append((b,cost))
            graph[b].append((a,cost))
        

    
    tSet = set()
    for i in range(t):
        tSet.add(int(input())) 
    
    INF = int(1e9)
    distance = [ INF for i in range(n+1)]
    def dijkstra(start):
        Q = []
        distance[start] = 0
        heapq.heappush(Q, (0, start))

        useGH = [False for i in range(n+1)] # GH를 쓰는 node들 기록
        while Q:
            dist, now = heapq.heappop(Q)
            if dist > distance[now] :
                continue

            for next , cost in graph[now]:
                newCost = dist + cost
                if distance[next] > newCost: # 갱신 시
                    distance[next] = newCost
                    heapq.heappush(Q, (newCost, next))
                    if (now in [g,h] and next in [g,h]) or useGH[now]:
                        useGH[next] = True
                    else:
                        useGH[next] = False
    
        resultList = []
        for i in tSet:
            if useGH[i]:
                resultList.append(i)
        resultList.sort()
        print(*resultList)
    
    dijkstra(s)
                        