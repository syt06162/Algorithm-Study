from copy import deepcopy
import sys
input = sys.stdin.readline

st = input().strip()
N = int(input())

countList = [ [0 for i in range(26)] ]
counter = [0 for i in range(26)]
for i in range(len(st)):
    counter[ord(st[i])-ord('a')] += 1
    countList.append(counter[:])

# 테스트
for i in range(N):
    alpha, l, r = input().split()
    answer = countList[int(r)+1][ord(alpha) - ord('a')] - countList[int(l)][ord(alpha) - ord('a')]
    print(answer)
    