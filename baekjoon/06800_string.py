import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(list(input().split()))
lst.sort(key=lambda x: x[1])

st = input().strip()
result = ""
now = ""
while st:
    now += st[0]
    st = st[1:]

    findFlag = False
    for alpha, bin in lst:
        if bin==now:
            result += alpha
            findFlag = True
            break
    if findFlag:
        now = ""

print(result)