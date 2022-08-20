import sys

# with bisect
N = int(input())
Nlst = list(map(int, sys.stdin.readline().split()))
Nlst.sort()

M = int(input())
Mlst = list(map(int, sys.stdin.readline().split()))

def bisect(target: int, start, end):
    while start <= end:
        mid = (start + end) // 2
        if Nlst[mid] == target:
            return 1
        elif Nlst[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0
    
result = []
for i in range(M):
    result.append(bisect(Mlst[i], 0, N-1))
    
print(*result, end=" ")