def solution(users, emoticons):
    from itertools import product
    saleR = list(product([0,10,20,30,40], repeat=len(emoticons)))
    
    resultN = -1
    resultP = -1
    
    # 브루트포스 - 모든 세일률 
    for sale in saleR:
        
        nowN = 0
        nowP = 0
        
        # 각 유저마다 이 가격 어떻게 되는지 확인
        for userS, userP in users:
            userTotal = 0
            for j in range(len(sale)):
                if sale[j] >= userS:
                    userTotal += emoticons[j]*(1-sale[j]*0.01)
            # 가입
            if userTotal >= userP:
                nowN += 1
            else:
                nowP += userTotal
        if nowN > resultN or (nowN==resultN and nowP > resultP):
            resultN = nowN
            resultP = nowP
    return [resultN, resultP]
            