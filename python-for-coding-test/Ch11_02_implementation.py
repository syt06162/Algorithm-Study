# Ch11_02
# 핵심: 0이 계산식에 없으면 무조건 곱한다. 있으면 더한다.

import sys

st = input()

result = 0
tempSum = 0
for i in range(len(st)):
    if tempSum == 0:
        tempSum = int(st[i])

    # 0이 아니면 곱하고
    elif st[i] != '0':
        tempSum *= int(st[i])

    # 0이 있으면 더한다.
    else:
        result += tempSum
        tempSum = 0
result += tempSum

print(result)