from collections import deque
k = int(input())
w,h = map(int,input().split())
arr = []
for i in range(h):
    arr.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ddx = [-1,-2,-2,-1,1,2,2,1]
ddy = [-2,-1,1,2,2,1,-1,-2]
visited =[[[0]*31 for i in range(w)] for i in range(h)]
def bfs():
    q = deque([])
    q.append((0,0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,z,cnt = q.popleft()
        if x == h-1 and y == w-1:
            print(cnt)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if arr[nx][ny] == 1 or visited[nx][ny][z]:
                continue
            visited[nx][ny][z] = 1
            q.append((nx,ny,z,cnt+1))
        if z < k:
            for i in range(8):
                nx = x + ddx[i]
                ny = y + ddy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if arr[nx][ny] == 1 or visited[nx][ny][z+1]:
                    continue
                visited[nx][ny][z+1] = 1
                q.append((nx,ny,z+1,cnt+1))
    print(-1)
bfs()
