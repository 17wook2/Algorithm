n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sand = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
ans = 0
def spread(x,y,d):
    global ans
    # for row in arr:
    #     print(row)
    # print(ans)
    nx,ny = x+dx[d], y+dy[d]
    t = arr[nx][ny]
    if t == 0:
        return
    arr[nx][ny] = 0
    remain = t
    for i in range(5):
        for j in range(5):
            nnx = nx - 2 + i
            nny = ny - 2 + j
            # print(nnx,nny)
            if d == 0:
                si = 4 - j
                sj = i
            if d == 1:
                si = i
                sj = 4 - j
            if d == 2:
                si = j
                sj = 4 - i
            if d == 3:
                si = i
                sj = j
            if sand[si][sj] == 'a':
                alpha = [nnx,nny]
                spd = 0
            else:
                spd = int(t*0.01*sand[si][sj])
                remain -= spd
            if nnx < 0 or nnx >= n or nny < 0 or nny >= n:
                ans += spd
                continue
            else:
                arr[nnx][nny] += spd
    nx = alpha[0]
    ny = alpha[1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        ans += remain
    else:
        arr[nx][ny] += remain
def move():
    mid = n // 2
    x, y = mid, mid
    for i in range(1,n):
        if i % 2 == 1: ## 왼쪽 아래
                for j in [3,2]:
                    for _ in range(i):
                        spread(x,y,j)
                        x = x + dx[j]
                        y = y + dy[j]
        else:
            for j in [1,0]: # 오른쪽 위
                for _ in range(i):
                    spread(x,y,j)
                    x = x + dx[j]
                    y = y + dy[j]

    for i in range(n):
        spread(x,y,3)
        x = x + dx[3]
        y = y + dy[3]

move()
print(ans)

