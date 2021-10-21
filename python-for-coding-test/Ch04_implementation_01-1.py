import sys

N = int(input())
lst = list(sys.stdin.readline().split())
pos = [1,1]
for ch in lst:
    if ch == "R":
        if pos[0] != N:
            pos[0] += 1
    elif ch == "U":
        if pos[1] != 1:
            pos[1] -= 1
    elif ch == "D":
        if pos[1] != N:
            pos[1] += 1
    elif ch == "L":
        if pos[0] != 1:
            pos[0] -= 1

print(pos[1], pos[0])