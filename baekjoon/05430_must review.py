import sys
from collections import deque

T = int(input())

for i in range(T):
    command = list(sys.stdin.readline().strip())
    N = int(sys.stdin.readline())
    Q = sys.stdin.readline().strip()
    
    if N != 0:
        Q = deque(Q[1:-1].split(','))
    else:
        Q = deque([])
    
    flag = 0 # 정방향(popleft)=0, 역방향(pop)=1
    
    for ch in command:
        if ch == 'R': # R이면 방향 전환
            flag = (flag+1)%2
            continue

        if not Q: # D인데 Q가 비었음
            print("error")
            break
        else:
            if flag == 0:
                Q.popleft()
            else:
                Q.pop()
    else:
        if flag==1:
            Q.reverse()
        print('[' + ",".join(Q) + ']')
            