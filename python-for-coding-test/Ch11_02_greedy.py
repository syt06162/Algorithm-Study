# Ch11_02
# 핵심: 0이나 1이 계산식에 없으면 무조건 곱한다. 있으면 더한다.

import sys

st = input()

result = 0
for i in range(len(st)):
    if result == 0:
        result = int(st[i])

    # 0이나 1이 아니면 곱하고
    elif st[i] not in ['0', '1']:
        result *= int(st[i])

    # 0이나 1이 있으면 더한다.
    else:
        result += int(st[i])

print(result)