import sys

# with dict
N, M = map(int, sys.stdin.readline().split())

numToEng = dict()
engToNum = dict()
for i in range(1,N+1):
    st = sys.stdin.readline().strip()
    numToEng[i] = st
    engToNum[st] = i

nums = [str(i) for i in range(0,10)]
for i in range(M):
    st = sys.stdin.readline().strip()
    # 숫자면
    if st[0] in nums:
        print(numToEng[int(st)])
    # 문자면
    else:
        print(engToNum[st])
        