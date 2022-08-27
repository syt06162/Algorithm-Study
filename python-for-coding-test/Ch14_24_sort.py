# Ch13_24
# boj 18310
# 핵심: 중위수가 답이라는 것을 아는 것

import sys


N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

print(lst[(N-1)//2])