# Ch11_01
# 핵심: 정렬 후 앞에서 부터 만들 수 있으면 바로 그룹

import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
result = 0

group = []
for num in lst:
    group.append(num)

    # 그룹 만족하는 경우 - 1추가
    if group[-1] <= len(group):
        result += 1
        group = []

print(result)

