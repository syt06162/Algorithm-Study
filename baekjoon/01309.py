import sys
input = sys.stdin.readline

N = int(input())
dp_now = [1,1,1] 
dp_next = [-1,-1,-1]
for i in range(1,N):
    dp_next[0] = dp_now[0] + dp_now[1] + dp_now[2]
    dp_next[1] = dp_now[0] + dp_now[2]
    dp_next[2] = dp_now[0] + dp_now[1]
    dp_now = dp_next
    dp_next = [-1,-1,-1]
print(sum(dp_now)%9901) 