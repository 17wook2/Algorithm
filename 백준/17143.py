def simulate():
    temp = [[0]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0:
                x,y,s,d,z = i,j,arr[i][j][0], arr[i][j][1], arr[i][j][2]
                for _ in range(s):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        d = (d+2) % 4
                        x = x + dx[d]
                        y = y + dy[d]
                    else:
                        x = nx
                        y = ny
                if temp[x][y] == 0:
                    temp[x][y] = [s,d,z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [s,d,z]
    return temp



dx = [-1,0,1,0]
dy = [0,1,0,-1]
r,c,m = list(map(int,input().split()))
arr = [[0]*c for i in range(r)]
res = 0
for i in range(m):
    a,b,s,d,z = list(map(int,input().split()))
    if d == 1: d = 0
    elif d == 3: d = 1
    elif d == 4: d = 3
    arr[a-1][b-1] = [s,d,z]


for i in range(c):
    for j in range(r):
        if arr[j][i] != 0:
            res += arr[j][i][2]
            arr[j][i] = 0
            break
    arr = simulate()

print(res)