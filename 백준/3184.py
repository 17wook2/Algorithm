from collections import deque
r,c = list(map(int,input().split()))
arr = []
for i in range(r):
    arr.append(list(input()))
visited = [[0]*c for i in range(r)]
q = deque()
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and arr[i][j] != '#':
            q.append((i,j))
            cnt += 1
            visited[i][j] = cnt
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] != '#':
                        visited[nx][ny] = visited[x][y]
                        q.append((nx,ny))
s,w = 0,0
for k in range(1,cnt+1):
    o,v = 0,0
    for i in range(r):
        for j in range(c):
            if visited[i][j] == k:
                if arr[i][j] == 'v': v += 1
                elif arr[i][j] == 'o': o += 1
    if o > v: s += o
    else: w += v

print(s,w)
