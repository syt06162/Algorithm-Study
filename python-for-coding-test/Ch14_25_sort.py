# Ch14_25
# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 핵심: 0으로 나눌때는 예외처리

def solution(N, stages):
    # 현위치
    isIn = [0 for i in range(N+2)]
    for i in range(len(stages)):
        isIn[stages[i]] += 1
    
    # 거쳐간사람
    dodal = [i for i in isIn]
    for i in range(N+1, 0, -1):
        dodal[i-1] += dodal[i]
    
    rr = []
    for i in range(1, N+1):
        if dodal[i] != 0:
            rr.append((-(isIn[i]/dodal[i]),i))
        else:
            rr.append((0, i))
    rr.sort()
    result = [i[1] for i in rr]
    
    return result