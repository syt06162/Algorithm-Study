# Ch13_24
# boj 18310
# 핵심: 

import sys


N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
half = sum(lst)/N

i = 0
while lst[i]<half:
    i += 1

j = N-1
while lst[j]>half:
    j -= 1
print(half)
if (half - lst[j]) <= lst[i] - half:
    result = lst[j]
else:
    result = lst[i]
print(result)