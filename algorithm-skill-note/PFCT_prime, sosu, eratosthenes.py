# 에라토스테네스의 체, 여러개(범위)의 소수 구할때
def eratosthenes(x : int): # 1~x 까지의 소수 모두 구하기
    sosu = [True for i in range(0,x+1)]
    sosu[0] = sosu[1] = False
    for i in range(2, int(x**(1/2)) +1): #개선 1. x까지 볼 필요없이 루트x까지만 해도 됨
        if sosu[i] == True:
            j = i #개선 2. 어차피 i 이전의 i보다 작은 소수의 체에서 걸렀던 것들이 있으므로, i*i 부터 시작하면 됨
            while i*j <= x:
                sosu[i*j] = False
                j += 1

    for i in range(x+1):
        if sosu[i]: print(i, end=" ")
    print()

# eratosthenes(1)
# eratosthenes(10)
# eratosthenes(100)


# 한개의 수 소수판정
def is_prime_number(x: int):
    if x == 1: return False

    for i in range(2, int(x**(1/2)) + 1):
        if x%i == 0:
            return False
    return True

# for i in range(1, 18):
#     print(i, is_prime_number(i))