# Ch11_05
# 핵심: 이중 for문으로 그냥 반복
# 추가풀이: 조합으로도 풀 수 있다. nC2 - 중복가능수

import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        if lst[i] != lst[j]:
            result += 1
print(result)
