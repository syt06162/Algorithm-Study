import sys

N, M = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

mins = []
# 각 행마다 min 값들을 구해 mins 리스트에 저장하고, 그 중 최대값을 답으로 출력
for i in range(N):
    mins.append(min(lst[i]))

print(max(mins))