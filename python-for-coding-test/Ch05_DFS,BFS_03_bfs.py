import sys
from collections import deque

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().strip())))

def bfs(si,sj, n,m):

    Q = deque()
    count = 1
    Q.append((si,sj, count))

    while True:
        (i, j, count) = Q.popleft()
        if i<0 or i>n or j<0 or j>m or lst[i][j]==0:
            continue
        if (i,j) == (n,m):
            print(count)
            return
        #lst[i][j]=0 #주석 풀면 문제 조금 변형 시 (목적지가 다르다거나 그러면) 에러
        count += 1
        Q.append((i-1,j,count))
        Q.append((i,j-1,count))
        Q.append((i+1,j,count))
        Q.append((i,j+1,count))

bfs(0,0,N-1,M-1)

# for i in range(N):
#     print(*lst[i],sep="")
