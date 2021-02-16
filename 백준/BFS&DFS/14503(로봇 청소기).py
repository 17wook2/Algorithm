n,m = list(map(int,input().split()))
r,c,d = list(map(int,input().split()))
array = [list(map(int,input().split())) for i in range(n)]

dx = [-1,0,1,0] # 위 오 아 왼
dy = [0,1,0,-1]
answer = 0
def dfs(x,y,d):
    global answer
    if array[x][y] == 0:
        array[x][y] = 2
        answer += 1
    for _ in range(4):
        dt = (d + 3) % 4
        nx = x + dx[dt] # 왼쪽으로 회전 했을때 위치
        ny = y + dy[dt]
        if 0 <= nx < n and 0 <= ny < m:
            if array[nx][ny] == 0:
                dfs(nx,ny,dt)
                return
            d = dt
    dt = (d + 2) % 4 # 뒤로가는 방향
    nx = x + dx[dt]
    ny = y + dy[dt]
    if array[nx][ny] == 1: # 벽인경우
        return
    dfs(nx,ny,d)

dfs(r,c,d)
print(answer)




