r,c,k = list(map(int,input().split()))
arr = []
for i in range(r):
    row = list(input())
    arr.append(row)
visited = [[0]*c for i in range(r)]
visited[r-1][0] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 0
def go(x,y,cnt):
    global ans
    if x == 0 and y == c-1 and cnt == k:
        ans += 1
    if cnt > k: return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if visited[nx][ny]: continue
        if arr[nx][ny] == 'T': continue
        visited[nx][ny] = 1
        go(nx,ny,cnt+1)
        visited[nx][ny] = 0
go(r-1,0,1)
print(ans)
