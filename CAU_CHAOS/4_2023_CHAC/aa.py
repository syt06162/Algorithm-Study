import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

chan = 0
ban = 0
moo = 0
for i in range(N):
    if lst[i] == 1:
        chan += 1
    elif lst[i] == -1:
        ban += 1
    else:
        moo += 1

HALF = N/2
if moo >= HALF:
    print("INVALID")
else:
    if chan>ban:
        print("APPROVED")
    else:
        print("REJECTED")
