import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
byung = []
for i in range(M):
    a,b, danger = map(int, input().split())
    byung.append((i, a,b,danger))

student = []
aMax = -1
bMax = -1
for i in range(N):
    a,b= map(int, input().split())
    student.append((b,a))
    if a > aMax:
        aMax = a
    if b > bMax:
        bMax = b

dp = [[-1 for i in range(aMax+1)] for j in range(bMax+1)]
dp[0][0] = 0

# set
dpSet = [[set() for i in range(aMax+1)] for j in range(bMax+1)]

# dp
i=0
for j in range(1, aMax+1):
    for num,a,b,danger in byung:
        if b>i or a>j:
            continue
        if dp[i-b][j-a] < 0:
            continue
        if num in dpSet[i-b][j-a]:
            continue
        
        if dp[i][j] < danger + dp[i-b][j-a]:
            dp[i][j] = danger + dp[i-b][j-a]
            dpSet[i][j] = copy.deepcopy(dpSet[i-b][j-a])
            dpSet[i][j].add(num)

for i in range(1,bMax+1):
    for j in range(0, aMax+1):
        for num, a,b,danger in byung:
            if b>i or a >j:
                continue
            if dp[i-b][j-a] < 0:
                continue
            if num in dpSet[i-b][j-a]:
                continue
            
            if dp[i][j] < danger + dp[i-b][j-a]:
                dp[i][j] = danger + dp[i-b][j-a]
                dpSet[i][j] = copy.deepcopy(dpSet[i-b][j-a])
                dpSet[i][j].add(num)


studentResult = []
for i in range(N):
    danger = max(dp[student[i][0]][student[i][1]], 0)
    studentResult.append((i+1,danger))
studentResult.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(*studentResult[i])
        

