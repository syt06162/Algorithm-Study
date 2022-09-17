import sys
input = sys.stdin.readline

M, S = input().split(":")
M = int(M)
S = int(S)

isJoLi = False
result = 0
# 그리디 시작
if S >= 30:
    isJoLi = True
    result += 1
    S -= 30

# 초 더하기
result += S//10
# 분
result += M%10
result += M//10

if not isJoLi:
    result += 1

print(result)
