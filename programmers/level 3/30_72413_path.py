def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        graph[i][i] = 0
    
    # 입력
    for c,d,cost in fares:
        graph[c][d] = cost
        graph[d][c] = cost

    # 플로이드
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    result = INF
    # 1부터 n번째 점까지를 각각 합승 끝점이라고 가정하고, 총합을 구해봄
    for inter in [i for i in range(1,n+1)]:
        total = graph[s][inter] + graph[inter][a] + graph[inter][b]
        result = min(result, total)
    
    return result