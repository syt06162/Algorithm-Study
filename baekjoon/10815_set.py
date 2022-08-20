import sys

# with set
N = int(input())
Nlst = set(map(int, sys.stdin.readline().split()))

M = int(input())
Mlst = list(map(int, sys.stdin.readline().split()))

result = [0 for i in range(M)]
for i in range(M):
    if Mlst[i] in Nlst:
        result[i] += 1
print(*result, end=" ")