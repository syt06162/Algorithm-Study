import sys

def getMin(startI, startJ):
    case1_count = 0
    case2_count = 0
    for i in range(startI, startI+8):
        for j in range(startJ, startJ+8):
            if (i+j)%2==0:
                if lst[i][j]=="W": 
                    case1_count += 1
                else: case2_count += 1
            else:
                if lst[i][j]=="B":
                    case1_count += 1
                else: case2_count += 1
    return min(case1_count, case2_count)

N, M = map(int, sys.stdin.readline().split())
lst = [[] for i in range(N)]

for i in range(N):
    st = sys.stdin.readline()
    for j in range(M):
        lst[i].append(st[j])

minArr=[]
for i in range(N-7):
    for j in range(M-7):
        minArr.append(getMin(i,j))
print(min(minArr))