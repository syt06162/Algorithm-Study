import sys

N = int(input())

lst = []
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))
lst.sort(key = (lambda x: (x[1], x[0])))


count = 1
endtime = lst[0][1]
idx = 1
while idx<N:
    if lst[idx][0] >= endtime:
        count += 1
        endtime = lst[idx][1]
    idx += 1

print(count)