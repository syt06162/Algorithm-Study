# Ch11_04
# My _ 혼자 풀기
# 핵심: nowSum 값

import sys
N = int(input())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()

if coins[0] != 1:
    print(1)
else:
    nowSum = 0
    for i in range(len(coins)):
        nowSum += coins[i]
        # 마지막인 코인도 되는 경우: nowSum +1 이 답
        # 다음 코인이 자격미달인 경우: nowSum +1 이 답
        if i == len(coins)-1 or nowSum+1 < coins[i+1]:
            print(nowSum+1)
            break
       
        
        

