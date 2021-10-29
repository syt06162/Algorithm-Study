import sys
from collections import deque
import copy

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(graph, start_I, start_J, dest_I, dest_J):
    Q = deque()
    flag = 1 # 벽 부술 기회가 아직 1번 남음 (0이면 기회 없음)
    graph[start_I][start_J] = -1 
    count = 1
    visited = [copy.deepcopy(graph), copy.deepcopy(graph)] #visited[flag] 확인. flag 가 1이면 1번지의 visited를 사용
    Q.append((start_I, start_J, count, flag))

    while Q:
        i, j, count, flag = Q.popleft()
        if i==dest_I and j==dest_J:
            break

        for k in range(4):
            ni = i+di[k]   
            nj = j+dj[k]
            if ni<0 or ni>dest_I or nj<0 or nj>dest_J: #범위 초과면 무시
                continue
            if visited[flag][ni][nj]==1: #벽일때는 flag가 1이면 무조건 부순다. flag가 0이면 컨티뉴
                if flag==0:
                    continue
                else:
                    visited[flag][ni][nj] = -1
                    Q.append((ni,nj,count+1, 0)) #벽 부수기 사용했으니 이제 flag에 0 넣어줌
                    
            elif visited[flag][ni][nj]==0: 
                visited[flag][ni][nj] = -1
                Q.append((ni,nj,count+1, flag))

        if not Q:
            return -1

    return count

size_I, size_J = map(int, sys.stdin.readline().split())
graph = [] #처음 : 갈수있는길=0, 벽:1  ... 탐색중: 갈수있는길=0, 벽:1, 이미 간길:-1
for i in range(size_I):
    graph.append(list(map(int, sys.stdin.readline().strip())))

print(bfs(graph, 0, 0, size_I-1, size_J-1)) 

