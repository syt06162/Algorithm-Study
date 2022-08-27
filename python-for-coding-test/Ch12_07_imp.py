# Ch12_07

import sys

st = input()
N = len(st)//2

lsum = 0
rsum = 0
for i in range(N):
    lsum += int(st[i])
    rsum += int(st[N+i])
if lsum == rsum:
    print("LUCKY")
else:
    print("READY")
