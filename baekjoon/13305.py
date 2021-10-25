import sys

N = int(input())

dis = list(map(int, sys.stdin.readline().split())) # [다음 도시까지의 거리]
price = list(map(int, sys.stdin.readline().split())) # [리터당 가격]

dis.append(0) #종료를 위해 마지막에 0을 붙임
price.append(0) #종료를 위해 마지막에 0을 붙임

currentIdx = 0
nextIdx = 1

result = 0
while currentIdx != len(price)-1:
    # 현위치 가격보다 더 싼 가격이 있는 곳까지 거리만 기름을 넣는다.
    while True: 
        if price[nextIdx] >= price[currentIdx]:
            nextIdx += 1
        else:
            break
    result += sum(dis[currentIdx:nextIdx]) * price[currentIdx]
    currentIdx = nextIdx
    nextIdx += 1

print(result)