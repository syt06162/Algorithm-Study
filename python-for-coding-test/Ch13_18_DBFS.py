# Ch13_18
# https://school.programmers.co.kr/learn/courses/30/lessons/60058
# 핵심: 멘붕하지않고 재귀함수 잘 구현

def solution(p):
    return fun(p)
    
def isCorrect(p):
    leftCount = 0
    for i in p:
        if i=="(":
            leftCount += 1
        else:
            leftCount -= 1
            
        if leftCount <0:
            return False
    return True

def toggle(p):
    now = ""
    for i in p:
        if i =="(":
            now += ")"
        else:
            now += "("
    return now
    
def fun(p):
    if isCorrect(p) == True: 
        return p
    
    # 2단계
    leftCount = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] =="(":
            leftCount += 1
        else:
            leftCount -= 1
        u += p[i]
        if leftCount == 0:
            break
    v = p[i+1:]
    
    # 3단계
    if isCorrect(u) == True:
        return u + fun(v)
    
    # 4단계
    return "(" + fun(v) + ")" + toggle(u[1:-1])
    
    