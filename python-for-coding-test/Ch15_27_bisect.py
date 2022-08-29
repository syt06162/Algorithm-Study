# Ch15_27

import sys

N, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

import bisect

l = bisect.bisect_left(nums, x)
r = bisect.bisect_right(nums, x)

sub = r-l
if sub!=0:
    print(sub)
else:
    print(-1)