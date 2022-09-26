import sys
input = sys.stdin.readline

N = int(input())
graph = dict()
for i in range(N):
    a,b,c = input().split()
    graph[a] = [b,c]

# 전위 순회
def preOrder(now):
    if now==".":
        return
    else:
        print(now, end="")
        preOrder(graph[now][0])
        preOrder(graph[now][1])
        
# 중위 순회
def inOrder(now):
    if now==".":
        return
    else:
        inOrder(graph[now][0])
        print(now, end="")
        inOrder(graph[now][1])

# 후위 순회
def postOrder(now):
    if now==".":
        return
    else:
        postOrder(graph[now][0])
        postOrder(graph[now][1])
        print(now, end="")
        
preOrder("A")
print()
inOrder("A")
print()
postOrder("A")