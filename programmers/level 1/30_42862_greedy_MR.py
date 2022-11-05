def solution(n, lost, reserve):
    count = n-len(lost)
    rSet = set(reserve)
    remover = []
    lost.sort() # sort 되어서 온다는 말이 없음!
    
    # 잃고 가져온 친구는 미리처리
    for l in lost:
        if l in rSet:
            rSet.remove(l)
            count += 1
        else:
            remover.append(l)
    
    # 그리디 - 앞부터
    for l in remover:
        if l-1 in rSet:
            rSet.remove(l-1)
            count += 1
        elif l+1 in rSet:
            rSet.remove(l+1)
            count += 1
    return count