# Ch18_45
# 위상정렬 끝판왕

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    before = list(map(int, input().split()))

    # 2차원 인접행렬, indegree 선언
    indegree = [0 for i in range(N+1)]
    graph = [[False for i in range(N+1)] for j in range(N+1)]
    for i in range(0,N):
        for j in range(i+1, N):
            graph[before[i]][before[j]] = True
            indegree[before[j]] += 1
            
    # 뒤바뀐 순서들은 뒤집고 indegree도 반전
    M = int(input())
    for i in range(M):
        a,b = map(int, input().split())
        if graph[a][b] == True:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1

    # 위상정렬 시작
    Q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            Q.append(i)
    
    result = []
    hasCycle = False
    for _1 in range(N): # 노드 수만큼 반복하는 것이 정상적
        if len(Q) == 0:
            hasCycle = True
            break

        now = Q.popleft()
        result.append(now)
        for i in range(1,N+1):
            if graph[now][i] == True:
                indegree[i] -= 1
                if indegree[i] == 0:
                    Q.append(i)
    
    # 결과 출력
    if hasCycle:
        print("IMPOSSIBLE")
    else:
        print(*result)

