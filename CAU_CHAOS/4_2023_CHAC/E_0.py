import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

INF = int(1e9)
hubo = []
# all L 전략
ans1 = -1
for i in range(N-1, -1, -1):
    if lst[i] == 1:
        ans1 = i+1
        break

# all R 전략
ans2 = -1
for i in range(0, N, 1):
    if lst[i] == 1:
        ans2 = N-i
        break

hubo.append(ans1)
hubo.append(ans2)


if N%2==1 and lst[N//2] == 1:
    pass
else:
    gyung = N/2
    if int(gyung) == gyung:
        gyung -= 0.5

    leftLast = -1
    i = 0
    while i < gyung:
        if lst[i] == 1:
            leftLast = i
        i+=1

    rightLast = -1
    i = N-1
    while i > gyung:
        if lst[i] == 1:
            rightLast = i
        i-=1
    
    if leftLast==-1 or rightLast==-1:
        pass
    else:
        leftLast += 1
        rightLast = N - rightLast
        ans3 = leftLast*2 + rightLast
        ans4 = leftLast + rightLast*2
        hubo.append(ans3)
        hubo.append(ans4)

minVal = INF
minIdx = INF
for i in range(len(hubo)):
    if hubo[i] < minVal:
        minVal = hubo[i]
        minIdx = i

print(minVal)
if minIdx==0:
    print("L"*minVal)
elif minIdx==1:
    print("R"*minVal)
elif minIdx==2:
    print("L"*leftLast+"R"*(rightLast + leftLast))
else: 
    print("R"*(rightLast)+"L"*(leftLast+rightLast))

if minIdx == INF or minIdx == -1:
    print("wrong!!")
print(hubo)