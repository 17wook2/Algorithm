from collections import deque
import math
r,c,k = list(map(int,input().split()))
arr = []
for i in range(r):
    arr.append(list(map(int,input())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque([])
q.append((0,0,0))
visited = [[[math.inf]*12 for i in range(c)] for i in range(r)]
visited[0][0][0] = 0
while q:
    x,y,cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] == 0:
                if visited[nx][ny][cnt] <= visited[x][y][cnt] + 1: continue
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                q.append((nx,ny,cnt))
            elif arr[nx][ny] == 1:
                if cnt >= k: continue
                if visited[nx][ny][cnt+1] <= visited[x][y][cnt] + 1: continue
                visited[nx][ny][cnt+1] = visited[x][y][cnt] + 1
                q.append((nx,ny,cnt+1))

ans = min(visited[r-1][c-1])+1
if ans == math.inf:
    print(-1)
else:
    print(ans)
