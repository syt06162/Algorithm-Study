import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))  # 띄어쓰기 구분
    board.append(list(map(int, input().strip())))  # 띄어쓰기 없이

lst = list(map(int, input().split()))