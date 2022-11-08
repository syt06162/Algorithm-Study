def solution(N, edge):
    # 다익스트라 해서 맥스 구하고 맥스 카운트
    
    graph = [[] for i in range(N+1)]
    INF = int(1e9)
    distance = [INF for i in range(N+1)]
    #그래프 추가ㅓ
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    #다익스트라
    import heapq
    Q = []
    distance[1] = 0
    heapq.heappush(Q,(0, 1)) #거리, 노드
    while Q:
        dis, now = heapq.heappop(Q)
        if dis > distance[now]:
            continue
        
        for next in graph[now]:
            cost = dis + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q,(cost, next))
    
    # 최대값 구하기
    val = -1
    for i in range(2, N+1):
        val = max(val, distance[i])
    
    # 최대값 세기
    result = 0
    for i in range(2, N+1):
        if distance[i] == val:
            result += 1
            
    print(distance)
    return result