from copy import deepcopy

maxResult = 0

def solution(info, edges):
    N = len(info) #info 0양, 1늑
    graph = [[] for i in range(N)] 
    
    for a,b in edges:
        graph[a].append(b)
    
    visited = [False for i in range(N)]
    
    def dfs(now, sheep, wolf, cango, visited):
        global maxResult

        cango = deepcopy(cango)
        visited = deepcopy(visited)
        visited[now] = True

        if info[now] == 0: # 양
            sheep += 1
            maxResult = max(maxResult, sheep)
        else:
            wolf += 1
            if wolf >= sheep:
                return

        for next in graph[now]:
            cango.append(next)

        for next in cango:
            if not visited[next]:
                dfs(next, sheep, wolf, cango, visited)

    dfs(0,0,0,[0],visited)
    
    return maxResult
            
    
    
