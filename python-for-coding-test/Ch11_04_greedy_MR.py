# Ch11_04
# MR _ 답지 보고 다시 풀기
# 핵심: target 값

import sys
N = int(input())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()

target = 1
for coin in coins:
    if coin > target:
        break
    else:
        target += coin
print(target)
        

