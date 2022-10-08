D, N = map(int, input().split())
oven = list(map(int, input().split()))
smallest = [oven[0]] #현재까지 최소크기, like dp
for i in range(1, D):
    smallest.append( min(smallest[i-1], oven[i]))
pizza = list(map(int, input().split()))
pizza.reverse()

# 피자 넣기 과정 - 오븐 맨아래부터
nowOvenIdx = D-1
nowPizzaIdx = N-1
while nowPizzaIdx >= 0:
    #최하단 오븐 찾기
    while nowOvenIdx >= 0 and pizza[nowPizzaIdx] > smallest[nowOvenIdx]:
        nowOvenIdx -= 1
    #거기에 피자넣기 - 넘칠경우 불가
    if nowOvenIdx>=0:
        nowPizzaIdx -= 1
        nowOvenIdx -= 1
    else:
        print(0)
        break

# 다돌았으면 다넣은것.
else:
    print(nowOvenIdx+1 + 1)

