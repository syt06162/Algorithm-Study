# Ch15_27

import sys

N, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

import bisect

l = bisect.bisect_left(nums, x) # 첫 좌표
r = bisect.bisect_right(nums, x) # 마지막 좌표 + 1

sub = r-l
if sub!=0:
    print(sub)
else:
    print(-1)