def solution(arr):
    N = len(arr)
    result = N
    
    hasLeft = [0 for i in range(N)]
    hasRight = [0 for i in range(N)]
    
    # left 부터 갱신
    minVal = arr[0]
    for i in range(1,N):
        if arr[i] < minVal:
            minVal = arr[i]
        else:
            hasLeft[i] = 1
    
    minVal = arr[N-1]
    for i in range(N-2, -1, -1):
        if arr[i] < minVal:
            minVal = arr[i]
        else:
            hasRight[i] = 1
    
    # 안되는거 빼기 - 양쪽에 본인보다 작은 수
    for i in range(N):
        if hasLeft[i] + hasRight[i] == 2:
            result -= 1
    return result
    