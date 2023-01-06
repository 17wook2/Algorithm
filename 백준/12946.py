import sys
sys.setrecursionlimit(10**5)
n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
dx = [-1,-1,0,1,1,0]
dy = [0,1,1,0,-1,-1]
ans = 0
visited = [[-1]*n for i in range(n)]
def solve(x,y,cnt):
    global ans
    visited[x][y] = cnt
    ans = max(ans,1)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'X':
           if visited[nx][ny] == -1:
               if cnt == 1:
                   solve(nx,ny,2)
               elif cnt == 2:
                   solve(nx,ny,1)
           ans = max(ans,2)
           if visited[nx][ny] == cnt:
               visited[x][y] = 3
               ans = max(ans,3)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X' and visited[i][j] == -1:
            solve(i,j,1)

print(ans)