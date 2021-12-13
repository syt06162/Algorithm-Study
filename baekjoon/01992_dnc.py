import sys

N = int(input())
lst = []
for i in range(N):
    lst.append(sys.stdin.readline().strip())

def qt( posI, posJ, size):
    c = lst[posI][posJ]
    if size == 1:
        print(c, end="")
        return

    for i in range(posI, posI+size):
        for j in range(posJ, posJ+size):
            if lst[i][j] != c:
                h = size//2
                print("(", end="")
                qt(posI, posJ, h)
                qt(posI, posJ + h, h)
                qt(posI + h, posJ, h)
                qt(posI + h, posJ + h, h)
                print(")", end="")
                return

    print(c, end="")


qt(0,0,N)