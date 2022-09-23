def solution(begin, end):
    # 소수면 1 리턴,아니면 약수 중 가장 작은수로 나눈 값 리턴
    
    result = []
    for now in range(begin, end+1):
        
        for i in range(2, int(now**(1/2))+1):
            if now%i==0 and now//i <= 10000000:
                result.append(now//i)
                break
        else:
            result.append(1)
    
    if begin==1:
        result[0] = 0
        
    return result


    