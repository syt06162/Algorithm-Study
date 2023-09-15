import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

if M <=3:
    ans = N//3 + 1
    if N%3==0:
        ans -= 1
    print(ans)
    exit()

isStair = [False for i in range(N)]
before = lst[-1]
streak = 1
for i in range(N-2, -1, -1):
    streak += 1
    if abs(before - lst[i]) != 1:
        streak = 1
    
    if streak >= M:
        isStair[i] = True
    before = lst[i]

dp = [-1 for i in range(N)] +[0]
cnt3 = 0
dpv = 1
for i in range(N-1, N-M, -1):
    if cnt3 == 3:
        dpv += 1
        cnt3 = 0
    dp[i] = dpv
    
    cnt3 += 1
    
# print(dp)

for i in range(N-M+1, -1, -1):
    dp[i] = min(dp[i+1], dp[i+2], dp[i+3]) + 1
    if isStair[i]:
        dp[i] = min(dp[i], dp[i+M] + 1)

# print(dp)
print(dp[0])




