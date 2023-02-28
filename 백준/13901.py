r,c = list(map(int,input().split()))
arr = [[0]*c for i in range(r)]
visited = [[0]*c for i in range(r)]
k = int(input())
for i in range(k):
    x,y = list(map(int,input().split()))
    arr[x][y] = 1
sx,sy = list(map(int,input().split()))
directions = list(map(int,input().split()))
visited[sx][sy] = 1
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
check = True
while check:
    check = False
    for direction in directions:
        while True:
            nx = sx + dx[direction]
            ny = sy + dy[direction]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] != 1:
                check = True
                visited[nx][ny] = 1
                sx = nx; sy = ny
            else:
                break
print(sx,sy)