# Ch15_29
# boj 2110
# 핵심 : gap을 bisect 처리 하는 것... 이런 생각을 하는 것..

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
nums = []
for i in range(N):
    nums.append(int(input()))
nums.sort()

gapStart = 1
gapEnd = nums[-1] - nums[0]

result = 1
while gapStart <= gapEnd:
    gapMid = (gapStart + gapEnd) // 2
    
    # gapMid 크기로 확인
    inter = int(1e9) + 1
    Ccount = 0

    for i in range(N):
        if i!= 0:
            inter += nums[i] - nums[i-1]
        # 설치
        if inter >= gapMid:
            inter = 0
            Ccount += 1
            
    if Ccount >= C:
        result = max(result, gapMid)
        gapStart = gapMid + 1
    else:
        gapEnd = gapMid - 1
print(result)
    