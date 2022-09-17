import sys
input = sys.stdin.readline

N = int(input())
ori = str(bin(N))[2:]
ori32 = ""
for i in range(len(ori), 32):
    ori32 += "0"
ori32 += ori

# 보수
bosu32 = []
for i in range(0,32):
    s =ori32[i]
    if s=="0":
        bosu32.append("1")
    else:
        bosu32.append("0")

for i in range(31,-1,-1):
    if bosu32[i]=="0":
        bosu32[i]="1"
        break
    else:
        bosu32[i]="0"

result = 0
for i in range(0,31):
    if bosu32[i]!=ori32[i]:
        result+=1
print(result)