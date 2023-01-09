def solution(cap, n, dList, pList):
    # 뒤 포인터
    dPtr = n-1
    pPtr = n-1
    while dPtr>=0 and dList[dPtr] == 0:
        dPtr -= 1
    while pPtr>=0 and pList[pPtr] == 0:
        pPtr -= 1
        
    result = 0
    while dPtr!=-1 or pPtr!=-1:
        pos = max(dPtr, pPtr)
        result += (pos+1)*2

        # d 다음 장소 확인
        dCap = cap
        while dCap > 0:
            if dPtr == -1:
                break
            elif dList[dPtr] == 0:
                dPtr -= 1
            else:
                dCap -= 1
                dList[dPtr] -= 1
        while dPtr>=0 and dList[dPtr] == 0:
            dPtr -= 1

        # p 다음 장소 구하기
        pCap = cap
        while pCap > 0:
            if pPtr == -1:
                break
            elif pList[pPtr] == 0:
                pPtr -= 1
            else:
                pCap -= 1
                pList[pPtr] -= 1
        while pPtr>=0 and pList[pPtr] == 0:
            pPtr -= 1
            
    return result
        
    