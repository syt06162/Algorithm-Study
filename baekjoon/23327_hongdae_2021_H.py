import sys

N, Q = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

sums = [0]
for i in range(N):
    sums.append(sums[i]+lst[i])

sqsums = [0]
for i in range(N):
    sqsums.append(sqsums[i]+lst[i]*lst[i])

for i in range(Q):
    start, end = map(int, sys.stdin.readline().split())

    a = sums[end]-sums[start-1]
    b = sqsums[end]-sqsums[start-1]

    print((a*a-b)//2)