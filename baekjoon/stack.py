class Stack:
    # push(x) -> x를 stack에 추가
    # pop() -> stack[-1] 제거하고 반환, 빈 stack이면 ERRVAL 반환
    # size() -> stack 원소 개수 반환
    # empty() -> 빈 stack이면 1, 아니면 0 반환
    # peer() -> stack[-1] 반환, 빈 stack이면 ERRVAL 반환
    
    def __init__(self, ERRVAL=-1):
        # pop, peer 연산시 빈 스택인 경우 return ERRVAL
        self.stack = []
        self.ERRVAL = ERRVAL

    def push(self, X :int):
        self.stack.append(X)
        
    def pop(self):
        if not self.stack:
            return self.ERRVAL
        else:
            return self.stack.pop()

    def size(self):
        print(len(self.stack))

    def empty(self):
        if not self.stack:
            return 1
        else: return 0

    def peer(self):
        if not self.stack:
            return self.ERRVAL
        else:
            return self.stack[-1]