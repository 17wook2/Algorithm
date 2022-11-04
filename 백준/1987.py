import sys
input = sys.stdin.readline
r,c = list(map(int,input().split()))
arr = []
for i in range(r):
    arr.append(list(input()))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = set()
visited.add(arr[0][0])
ans = 1
def dfs(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in visited:
            visited.add(arr[nx][ny])
            dfs(nx,ny,cnt+1)
            visited.remove(arr[nx][ny])
dfs(0,0,1)
print(ans)