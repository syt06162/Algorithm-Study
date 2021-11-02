import sys
from collections import deque

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(lst, iniQ):
    
    Q = deque()
    while iniQ: #초기 토마토 좌표들을 Q에 넣어줌
        Q.append(iniQ.pop())

    Q.append((-1,-1)) #1회전 할 때마다 count를 증가시키기 위해 넣어줌
    count = -1

    while Q:
        i,j = Q.popleft()
        if (i,j)==(-1,-1): #1회전이 됐다는 의미이므로 count증가, 만약 Q가 비어있으면 종료, 아직 남아있다면 다시 Q에 넣음
            count += 1
            if Q: Q.append((-1,-1))
            continue

        for k in range(4):
            nI = i+di[k]
            nJ = j+dj[k]
            if nI<0 or nI>=sizeI or nJ<0 or nJ>=sizeJ:
                continue
            if lst[nI][nJ]==0: #새로운 좌표에 아직 안 익은 토마토가 있을때만 Q에 삽입
                lst[nI][nJ]=1
                Q.append((nI,nJ))
    
    return count


sizeJ, sizeI = map(int,sys.stdin.readline().split())
lst = []
for i in range(sizeI):
    lst.append(list(map(int, sys.stdin.readline().split())))

count = 0
iniQ = [] #초기에 토마토(1)가 있는 좌표들 기록 큐
for i in range(sizeI):
    for j in range(sizeJ):
        if lst[i][j]==1:
            iniQ.append((i,j)) 

count = bfs(lst, iniQ)

flag = 1
for i in range(sizeI):
    for j in range(sizeJ):
        if lst[i][j]==0: #0인 토마토가 하나라도 있으면 바로 -1 출력
            flag = 0
            print(-1)
            break
    if flag == 0:
        break
if flag==1: #0인 토마토가 하나도 없다면 count 출력
    print(count)
