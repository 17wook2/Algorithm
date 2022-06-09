import copy
array = [[] for i in range(4)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
ans = 0
for i in range(4):
    lst = list(map(int,input().split()))
    fish = []
    for j in range(0,8,2):
        fish.append([lst[j], lst[j+1]-1])
    array[i] = fish

def move_fish(sx,sy,board):
    for f in range(1,17):
        fx,fy = -1,-1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == f:
                    fx,fy = i,j
                    break
        if fx == -1 and fy == -1:
            continue
        fd = board[fx][fy][1]
        for i in range(8):
            nd = (fd+i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                board[fx][fy][1] = nd
                board[nx][ny], board[fx][fy] = board[fx][fy], board[nx][ny]
                break

def dfs(sx,sy,score,board):
    global ans
    score += board[sx][sy][0]
    board[sx][sy][0] = 0
    d = board[sx][sy][1]
    ans = max(ans,score)
    move_fish(sx,sy,board)
    for i in range(1,5):
        nx = sx + dx[d]*i
        ny = sy + dy[d]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] > 0:
            dfs(nx,ny,score,copy.deepcopy(board))

dfs(0,0,0,array)
print(ans)
