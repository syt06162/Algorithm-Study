A, B, C = map(int, input().split())
lst = [-1]*31 
# 2의 31승이 2147483648이므로
# lst[i]는 (A의 2**i승) % C 의 값을 저장

lst[0] = A%C
for i in range(1, 31):
    lst[i] = (lst[i-1] ** 2) % C

B_2digit = list(map(int, bin(B)[2:][::-1])) # B를 2진수로 바꾼 값을 뒤집은것

result = 1
for i in range(len(B_2digit)):
    if B_2digit[i]==0:
        continue
    result = (result * lst[i]) % C

print(result)