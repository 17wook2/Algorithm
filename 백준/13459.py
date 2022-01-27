from collections import deque
n,m = list(map(int,input().split()))
board = []
for i in range(n):
    tmp = list(input())
    board.append(tmp)
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red = (i,j)
        elif board[i][j] == 'B':
            blue = (i,j)

## d = 0부터 위왼아오
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited= [[[[0]*m for i in range(n)] for i in range(m)] for i in range(n)]
def move(x,y, direction):
    cnt = 0
    while board[x+dx[direction]][y + dy[direction]] != '#' and board[x][y] != 'O':
        x += dx[direction]
        y += dy[direction]
        cnt += 1
    return x,y,cnt

def bfs():
    q = deque([])
    q.append((red[0],red[1],blue[0],blue[1],0))
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt >= 10:
            break
        for i in range(4):
            nrx,nry,red_cnt = move(rx,ry,i)
            nbx,nby,blue_cnt = move(bx,by,i)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return 1
            if nrx == nbx and nry == nby:  ## 두점 같으면
                if red_cnt > blue_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                q.append((nrx,nry,nbx,nby,cnt + 1))
    return 0

print(bfs())