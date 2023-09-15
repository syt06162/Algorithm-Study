from collections import deque
# dfs, bfs

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 가능하면 visited를 꼭 쓰자! 안그러면 무한루프에 빠지거나, 엄청난 시간초과가 뜬다!
# 둘다 쓸 수 있는 상황이면 보통 bfs가 더 빠른 것 같다.


### dfs 는 심플하게 재귀
visited = [False for i in range(8 + 1)]

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

dfs(1) # 1 2 7 6 8 3 4 5



# bfs에서 중요한 점은, visited=True 를 어디에 처리할지이다.
# Q에서 pop 하고나서 처리할 경우 여러개의 같은 것이 중복으로 Q에 들어가게 될 수도 있으니,
### 반드시 for문 안에서 Q에 삽입(append) 직전에 visited를 True로 바꾸자.

visited = [False for i in range(8 + 1)]

def bfs(v):
    from collections import deque

    Q = deque()
    visited[v] = True
    Q.append(v)

    while Q:
        now = Q.popleft()
        print(now, end=" ")
        
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True # append 직전에 visited True!
                Q.append(next)

bfs(1) # 1 2 3 8 7 4 5 6

