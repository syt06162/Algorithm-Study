def solution(lottos, win_nums):
    zeroCount = 0
    correctCount = 0
    for n in lottos:
        if n == 0:
            zeroCount += 1
        elif n in win_nums:
            correctCount += 1
    # 순위
    winMax = zeroCount + correctCount
    winMin = correctCount
    if winMax >= 2:
        winMax = 7 - winMax
    else:
        winMax = 6
    if winMin >= 2:
        winMin = 7 - winMin
    else:
        winMin = 6
    
    return [winMax, winMin]
        
    