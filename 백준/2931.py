from collections import deque
r,c = map(int,input().split())
arr = []
sign = ['|','-','+','1','2','3','4']
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0]*c for i in range(r)]
bx=0; by=0; bdirection = []
def direction(s):
    if s == '|':
        return [0,2]
    elif s == 'M' or s == 'Z':
        return [0,1,2,3]
    elif s == '-':
        return [1,3]
    elif s == '+':
        return [0,1,2,3]
    elif s == '1':
        return [1,2]
    elif s == '2':
        return [0,1]
    elif s == '3':
        return [0,3]
    elif s == '4':
        return [2,3]

def bfs(x, y):
    global bx,by
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        dirs = direction(arr[x][y])
        for d in dirs:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == '.':
                    if arr[x][y] == 'M' or arr[x][y] == 'Z':
                        continue
                    bx,by = nx,ny
                    bdirection.append((d+2)%4)
                else:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

for i in range(r):
    row = list(input())
    for j in range(c):
        if row[j] == 'M':
            m = (i,j)
        elif row[j] == 'Z':
            z = (i,j)
    arr.append(row)
bfs(m[0],m[1])
bfs(z[0],z[1])

for i in range(r):
    for j in range(c):
        if arr[i][j] != '.' and not visited[i][j]:
            bfs(i,j)

bdirection = list(set(bdirection))
bdirection.sort()
for s in sign:
    if bdirection == direction(s):
        print(bx+1,by+1,s)


