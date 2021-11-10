import sys

N = int(input())
dp = [ [0, 0, 0] ]
for i in range(N): 
    R, G, B = map(int, sys.stdin.readline().split())
    minR = min( R+dp[i][1], R+dp[i][2])
    minG = min( G+dp[i][0], G+dp[i][2])
    minB = min( B+dp[i][0], B+dp[i][1])
    dp.append([minR, minG, minB])

print(min(dp[N]))