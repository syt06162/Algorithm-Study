# Ch12_14
# https://school.programmers.co.kr/learn/courses/30/lessons/60062?language=python3
# 핵심: weak 원형 배열을 두배로 늘려 일자로.

# 모두 확인하는데, 이는 start 인덱스를 하나씩 늘리며,
# dist는 "순열"로 모든 경우 테스트

def solution(n, weak, dist):
    # 두배 길이로 확장
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    from itertools import permutations
    
    result = len(dist) + 1
    for start in range(length):
        # start, end, now 는 weak 배열의 인덱스
        end = start + length - 1
        
        for perms in list(permutations(dist, len(dist))):
            count = 0
            now = start
            for nextFriend in perms:
                # 친구 충분하면, 종료
                if now > end:
                    break
                
                # 새 친구 영입
                position = weak[now] + nextFriend
                count += 1
                while now <= end and weak[now] <= position:
                    now += 1
            # 이 순열로 할 수 있을때만 최저 갱신
            if now>end:
                result = min(result, count)
    
    # 다 확인 후 리턴
    if result == len(dist)+1:
        return -1
    else:
        return result
            
    
    