# Ch11_03
# 핵심: 0연속, 1연속의 개수를 세서 더 적은 값이 답이다.

import sys

st = input()

streak_count = [0, 0] # 연속집합의 개수

before = st[0]
for i in range(1, len(st)):
    if before == st[i]:
        continue
    else:
        streak_count[int(before)] += 1
        before = st[i]
streak_count[int(before)] += 1

print(min(streak_count[0], streak_count[1]))