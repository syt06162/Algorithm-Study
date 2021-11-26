import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
dp_front = [1 for i in range(N)] #앞에서부터 증가하는 것을 기록하는 dp
dp_end = [1 for i in range(N)] #뒤에서부터 증가하는 것을 기록하는 dp

for i in range(1, N):
    for j in range(0,i):
        if lst[j] < lst[i] and dp_front[j] >= dp_front[i]:
            dp_front[i] = dp_front[j] + 1

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if lst[j] < lst[i] and dp_end[j] >= dp_end[i]:
            dp_end[i] = dp_end[j] + 1

dp_sum = [ (dp_front[i]+dp_end[i]-1) for i in range(N)]
print(max(dp_sum))