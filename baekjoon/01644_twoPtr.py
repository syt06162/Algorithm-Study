# 큰 흐름
# 1. 에라토스테네스로 입력값 N 보다 작거나 같은 소수들을 구한다.
# 2. 그 소수들의 시작부터 부분합을 구한다 (시간 단축을 위함)
# 3. 투포인터 알고리즘으로 최종을 구한다.

def erat(num: int):
    # num 이하의 소수들만 구한 리스트
    result = []
    tempLst = [ True for _ in range(0, num+1)] # 0번지, 1번지는 사용하지 않음
    for i in range(2, num+1):
        if tempLst[i] == False:
            continue
        else:
            result.append(i)
            j = i*i
            while j<= num:
                tempLst[j] = False
                j += i

    return result


N = int(input())

sosuLst = erat(N) 
length = len(sosuLst)
hapLst = [0]
for i in range(0, length):
    hapLst.append(sosuLst[i] + hapLst[i])


result = 0
left = 0
right = 1 # left부터 right-1까지 합을 구해서 N 이랑 같으면 result +1
while left <= length:
    nowHap = hapLst[right-1] - hapLst[left]
    if nowHap == N:
        result += 1
    
    if nowHap < N and right <= length:
        right += 1
    else:
        left += 1

        
print(result)