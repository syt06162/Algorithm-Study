# Ch12_09
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 기본 코드가 제공되므로 반드시 해당 링크에서 실행

def solution(s):
    length = len(s)
    
    min_len = length
    
    for i in range(1, length):
        result = ""
        
        start = 0
        while start + i < length:
            subS = s[start:start + i]
            count = 1

            j = start + i
            while j+i <= length and s[j:j+i] == subS:
                j += i
                count += 1
                
            if count == 1:
                result += subS
            else:
                result += str(count) + subS
            
            start += i*count
        else:
            result += s[start:]
            
        min_len = min(min_len, len(result))
        
    return min_len
        