# Ch11_06
# https://school.programmers.co.kr/learn/courses/30/lessons/42891
# 기본 코드가 제공되므로 반드시 해당 링크에서 실행

import heapq

def solution(food_times, k):
    # -1인 경우
    if sum(food_times) <= k:
        return -1
    
    length = len(food_times) # 현재 남은 길이를 뜻함. 바뀔 수 있음
    
    Q = []
    for i in range(length):
        heapq.heappush(Q, (food_times[i], i)) # 음식수, 인덱스
        
    time = 0 # 돌아간 바퀴 수
    while True: 
        
        n, idx = heapq.heappop(Q)
        realN = n - time # realN = 실제n값에서 돌아간 바퀴수를 빼야 진짜 남은 음식수
        
        # 이 접시 다 먹을동안 돌아도 안끝나면
        if realN*length <= k:
            time += realN # realN 바퀴만큼 돌기
            k -= realN*length # 바퀴수*현재길이
            length -= 1 # 이제 이 음식은 다 먹은거니 접시 다음부터 카운트 안함
            
        # 이 접시 다 먹기전 종료면
        else:
            # Q에 남은 것들 다 index 기준으로 정렬 - 계산해서 리턴
            leftList = []
            leftList.append(idx)
            while Q:
                temp, idx = heapq.heappop(Q)
                leftList.append(idx)
            leftList.sort()
            return leftList[(k) % len(leftList)] + 1
            