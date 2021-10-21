pos = input()
x, y = ord(pos[0])-ord('a'), int(pos[1])-1

lst = []
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

for i in range(8):
    lst.append( [ x+dx[i], y+dy[i] ] )

cnt = 0
for x,y in lst:
    if x<0 or x>8 or y<0 or y>8:
        continue
    cnt += 1
print(cnt)

