stack = []

def solution(ingredient):
    count = 0
    
    for i in ingredient:
        stack.append(i)    
        if isComplete():
            for _ in range(4):
                stack.pop()
            count += 1
    return count
            
        
def isComplete():
    if len(stack) < 4 :
         return False
    
    if stack[-4]==1 and stack[-3]==2 and stack[-2]==3 and stack[-1]==1:
        return True
    return False
