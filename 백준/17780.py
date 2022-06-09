def simulate():
    cnt = 1
    while True:
        for x in range(k):
            move(x)
        if end_check():
            return cnt
        cnt += 1
        if cnt > 1000:
            return -1
def move(x):
    if check_can_move(x):
        r,c,d = horses[x]
        nx = r + dx[d]
        ny = c + dy[d]
        if out_of_bound(nx,ny) or board[nx][ny] == 2: ## 파란색이나 경계 밖
            d = (d + 2) % 4
            horses[x][2] = d
        nx = r + dx[d]
        ny = c + dy[d]
        if not out_of_bound(nx,ny) and board[nx][ny] == 0:
            stack = s_board[r][c]
            for s in stack:
                horses[s][0] = nx
                horses[s][1] = ny
            s_board[nx][ny].extend(stack)
            s_board[r][c] = []
        elif not out_of_bound(nx,ny) and board[nx][ny] == 1:
            stack = s_board[r][c]
            for s in stack:
                horses[s][0] = nx
                horses[s][1] = ny
            stack.reverse()
            s_board[nx][ny].extend(stack)
            s_board[r][c] = []


def check_can_move(x):
    r,c,d = horses[x]
    if s_board[r][c][0] == x:
        return True
    else:
        return False

def out_of_bound(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    else:
        return False

def end_check():
    for i in range(n):
        for j in range(n):
            if len(s_board[i][j]) >= 4:
                return True
    return False

n, k = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = []
horses = []
s_board = [[[]*n for i in range(n)] for i in range(n)]
for i in range(n):
    board.append(list(map(int,input().split())))
for idx in range(k):
    r,c,d = list(map(int,input().split()))
    r -= 1; c -=1
    if d == 2: d = 3
    elif d == 3: d = 0
    elif d == 4: d = 2
    horses.append([r,c,d])
    s_board[r][c].append(idx)

print(simulate())