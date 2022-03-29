from collections import deque
n = int(input())
arr = [[0]*2001 for i in range(2001)]
for i in range(n):
    pos = list(map(int,input().split()))
    pos = list(map(lambda x:(x+500)*2, pos))
    x1,y1,x2,y2 = pos
    for i in range(x1,x2+1):
        arr[i][y1] = 1
        arr[i][y2] = 1
    for i in range(y1,y2+1):
        arr[x1][i] = 1
        arr[x2][i] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 0:
            continue
        elif arr[i][j] == 1:
            cnt += 1
            queue = deque([])
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                arr[x][y] = 2
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < 2001 and 0 <= ny < 2001 and arr[nx][ny] == 1:
                       arr[nx][ny] = 2
                       queue.append((nx,ny))

if arr[1000][1000] == 2:
    cnt -= 1

print(cnt)
