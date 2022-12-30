def dfs(row,col):
    global cnt,check
    visited[row][col] = 1
    if col == c-1:
        check = True
        cnt += 1
        return
    else:
        for i in range(3):
            nx = row + dx[i]
            ny = col + 1
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == '.' and not visited[nx][ny]:
                    dfs(nx,ny)
                    if check:
                        return

check = False
dx = [-1,0,1]
r,c = map(int,input().split())
arr = []
visited = [[0]*c for i in range(r)]
cnt = 0
for i in range(r):
    arr.append(list(input()))

for i in range(r):
    dfs(i,0)
    check = False

print(cnt)