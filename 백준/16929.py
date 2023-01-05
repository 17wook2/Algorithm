n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
ans = 'No'
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(cnt,cur_x,cur_y):
    global ans
    if ans == 'Yes': return
    if cur_x == tx and cur_y == ty and cnt >= 4:
        ans = 'Yes'
        return True
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if arr[cur_x][cur_y] != arr[nx][ny]: continue
        if nx == tx and ny == ty and cnt >= 3:
            dfs(cnt+1, nx,ny)
        if visited[nx][ny]: continue
        visited[nx][ny] = 1
        dfs(cnt+1,nx,ny)
        visited[nx][ny] = 0
for i in range(n):
    for j in range(m):
        tx = i; ty = j
        visited = [[0]*m for i in range(n)]
        visited[i][j] = 1
        if dfs(1,i,j):
            print(ans)
            exit()
print(ans)