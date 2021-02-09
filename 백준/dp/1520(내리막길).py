m,n = list(map(int,input().split()))
array = [list(map(int,input().split())) for _ in range(m)]
visited = [[0 for __ in range(n)] for _ in range(m)]
# print(visited)
# print(array)
# dfs 로?
stack = [(0,0)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while stack:
    x,y = stack.pop()
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if array[nx][ny] < array[x][y]:
            stack.append((nx,ny))

def dfs(x,y):
