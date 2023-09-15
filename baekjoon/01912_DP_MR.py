import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

# 모두음
for i in range(1,N+1):
    if lst[i]>=0: 
        break
else:
    print(max(lst[1:]))
    exit()

dp_streak = [0 for i in range(N+1)]
dp_me = [0 for i in range(N+1)]

for i in range(1,N+1):
    dp_streak[i] = max(dp_streak[i-1] , dp_me[i-1]) + lst[i]
    dp_me[i] = lst[i]

a = max(dp_streak)
b = max(dp_me)
print(max(a,b))