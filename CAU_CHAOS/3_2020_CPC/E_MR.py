import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cube_state = list(map(int, input().split()))
switches = []
for ii in range(K):
    lst = list(map(int, input().split()))
    switch = [0 for i in range(N)]
    for i in lst[1:]:
        switch[i-1] = ii+1
    switches.append(switch)

# print(switches)

def list_add(lst1, lst2): # l1 바꿈
    for i in range(len(lst1)):
        lst1[i] += lst2[i]
        lst1[i] %= 5

def intList_to_str(lis):
    st = ""
    for i in lis:
        st += str(i)
    return st
        

dist_dict = dict()
now_list = cube_state

# Q 쓰고, visit 안한거는 not in, 한거는 in이다.
def bfs(cube_state):
    from collections import deque
    from copy import deepcopy

    Q = deque()
    nowState = intList_to_str(cube_state)
    dist_dict[nowState] = 0
    Q.append((cube_state, 0))

    while Q:
        now_list, distance = Q.popleft()
        distance += 1
        
        for switch in switches:
            temp = deepcopy(now_list)
            list_add(temp, switch)
            if min(temp) == max(temp):
                return distance
            
            temp_st = intList_to_str(temp)
            if temp_st in dist_dict:
                continue
            else:
                dist_dict[temp_st] = distance
                # print(temp_st, distance, dist_dict)
                Q.append((temp, distance))
    return -1

# print(dist_dict)
print(bfs(cube_state))
