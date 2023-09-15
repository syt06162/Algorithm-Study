import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
X1, X2, Y1, Y2 = map(int, input().split())

answer = "Lucky"
if B!= 0:
    for Xin in [X1, X2]: # x넣어 y체크
        y = (-A*Xin - C)/B
        if y<max(Y1,Y2) and y>min(Y1,Y2):
            print("Poor")
            exit()
        else:
            continue

if A!= 0:
    for Yin in [Y1, Y2]: # y넣어 x체크
        x = (-B*Yin - C)/A
        if x<max(X1,X2) and x>min(X1,X2):
            print("Poor")
            exit()
        else:
            continue

print(answer)