n,m = list(map(int,input().split()))
array = [list(map(int,input())) for i in range(n)]
# print(array)
stack = []
stack.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while stack:
    x,y = stack.pop()
    values = array[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=m:
            continue
        if array[nx][ny] == 0:
            continue
        if array[nx][ny] == 1 or values + 1 < array[nx][ny]:
            stack.append((nx,ny))
            array[nx][ny] = values + 1
print(array[-1][-1])

