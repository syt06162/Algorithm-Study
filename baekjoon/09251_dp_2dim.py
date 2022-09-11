import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
N1 = len(s1)
N2 = len(s2)

dp = [[0 for i in range(N1+1)] for i in range(N2+1)]
for i in range(1,N2+1):
    for j in range(1,N1+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N2][N1])
    
