import sys

N = int(input())

dis = list(map(int, sys.stdin.readline().split())) # [다음 도시까지의 거리]
price = list(map(int, sys.stdin.readline().split())) # [리터당 가격]

dis.append(0)
price.append(0)

currentIdx = 0
nextIdx = 1

result = 0
while currentIdx != len(price)-1:
    while True:
        if price[nextIdx] >= price[currentIdx]:
            nextIdx += 1
        else:
            break
    result += sum(dis[currentIdx:nextIdx]) * price[currentIdx]
    currentIdx = nextIdx
    nextIdx += 1

print(result)



# 10
# 1 2 3 4 3 2 1 2 3
# 5 4 2 3 4 1 6 4 2 3
