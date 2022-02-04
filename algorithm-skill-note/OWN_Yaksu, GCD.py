# math.gcd, math.lcm 도 있음.

def GCD(a, b):
    while b>0:
        a, b = b, a%b
    return a

def getGCD(*integers): 
    bound = min(integers)
    while bound > 0: 
        idx = 0
        while idx < len(integers):
            if integers[idx] % bound != 0:
                break
            idx += 1
        else:
            return bound
        bound -= 1
    return -1

def getYaksu(num):
    sosulst = []
    templst = []
    i = 1
    sq = int(num**(1/2))
    for i in range(1, sq+1):
        if num%i == 0:
            sosulst.append(i)
            templst.append(num//i)

    if templst[-1] == sosulst[-1]:
        templst.pop()

    while templst:
        sosulst.append(templst.pop())

    return sosulst

print(getGCD(1,2,3,4))
print(getGCD(4,6,8,10))

print(getGCD(1,2,3,1))

print(getGCD(1,2,1,1))

print(getGCD(1,0,2,3))