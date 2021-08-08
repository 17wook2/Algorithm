from collections import deque
n,m,k = list(map(int,input().split()))
fireballs = []
for i in range(m):
    fireballs.append(list(map(int,input().split())))



dx = [-1,-1,0,1,1,1,0,-1] ## 각각 방향 01234567
dy = [0,1,1,1,0,-1,-1,-1]
temp = []

for i in range(k):
    # print(fireballs)
    board = [[deque([]) for i in range(n)] for i in range(n)]
    for firball in fireballs: ## 파이어볼 이동
        r,c,m,s,d = firball ## 좌표,질량,이동칸수,방향
        r-=1; c-=1
        nx = r + dx[d] * s
        ny = c + dy[d] * s
        nx = (nx + n) % n
        ny = (ny + n) % n
        board[nx][ny].append((m,s,d))

    for x in range(n):
        for y in range(n):
            if board[x][y] != []:
                if len(board[x][y]) == 1:
                    m,s,d = board[x][y][0]
                    temp.append((x,y,m,s,d))
                elif len(board[x][y]) >= 2:
                    m,s,d = 0,0,0
                    for i in range(len(board[x][y])):
                        m += board[x][y][i][0]
                        s += board[x][y][i][1]
                        if board[x][y][i][2] % 2 == 0:
                            d -= 1
                        else:
                            d += 1
                    m //= 5
                    s //= len(board[x][y])
                    if abs(d) == len(board[x][y]): ## 모두 홀수거나 짝수
                        d = 0
                    else:
                        d = 1
                    board[x][y] = []
                    if m > 0:
                        for i in range(4):
                            temp.append((x,y,m,s,d+i*2))
                            board[x][y].append((m,s,d+i*2))
    fireballs = temp
    temp = []

ans = 0
for x in range(n):
    for y in range(n):
        if board[x][y] != []:
            for i in range(len(board[x][y])):
                ans += board[x][y][i][0]

print(ans)