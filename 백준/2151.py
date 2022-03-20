from collections import deque
n = int(input())
arr = []
door = []
mirror = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 5000
visited = [[[5000]*4 for i in range(n)] for i in range(n)]
for i in range(n):
    row = list(input())
    for j in range(n):
        if row[j] == '#':
            door.append((i,j))
        if row[j] == '!':
            mirror.append((i,j))
    arr.append(row)
queue = deque([])
x,y = door[0][0], door[0][1]
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '*':
        queue.append((x,y,i,0))
while queue:
    x,y,d,cnt = queue.popleft()
    if visited[x][y][d] <= cnt:
        continue
    visited[x][y][d] = cnt
    if x == door[1][0] and y == door[1][1]:
        ans = min(ans,cnt)
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '*':
        if arr[nx][ny] == '!': ## 거울 설치할지 안할지
            if d == 0 or d == 2:
                for nd in [1,3]:
                    queue.append((nx,ny,nd,cnt+1))
            if d == 1 or d == 3:
                for nd in [0,2]:
                    queue.append((nx,ny,nd,cnt+1))
        queue.append((nx,ny,d,cnt)) ## 거울 설치 안할때
print(ans)