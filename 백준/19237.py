def difuse():
    for i in range(n):
        for j in range(n):
            if board[i][j][0] != 0:
                if board[i][j][2] == 1:
                    board[i][j] = [0,0,0]
                else:
                    board[i][j][2] = board[i][j][2] - 1
def move():
    shark_after = []
    for x in range(n):
        for y in range(n):
            if board[x][y][0] != 0 and board[x][y][2] == k:
                f_number = board[x][y][0]
                pos = []
                pri = priority[f_number][board[x][y][1]]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny][0] == 0:
                        pos.append(i)
                if len(pos) > 0:
                    for pr in pri:
                        if pr in pos:
                            d = pr
                            break
                    shark_after.append([x,y,d,f_number])
                    continue
                pos = []
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny][0] == f_number:
                        pos.append(i)
                if len(pos) > 0:
                    for pr in pri:
                        if pr in pos:
                            d = pr
                            break
                    shark_after.append([x,y,d,f_number])
    difuse()
    shark_after.sort(key = lambda x:x[3])
    for shark in shark_after:
        x,y,d,f_num = shark
        nx = x + dx[d]
        ny = y + dy[d]
        if board[nx][ny][0] != 0 and f_num > board[nx][ny][0]:
            continue
        board[nx][ny][0] = f_num
        board[nx][ny][1] = d
        board[nx][ny][2] = k

def check():
    c = 0
    for i in range(n):
        for j in range(n):
            if board[i][j][0] != 0 and board[i][j][2] == k:
                c += 1
    if c == 1:
        return True
    else:
        return False

n,m,k = list(map(int,input().split()))
board = [[] for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(n):
        board[i].append([lst[j],0,0])
direction = list(map(int,input().split()))
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j][0] != 0:
            cnt += 1
            board[i][j][1] = direction[board[i][j][0]-1]-1
            board[i][j][2] = k
priority = [[]]
for i in range(cnt):
    x = []
    for j in range(4):
        lst = list(map(int,input().split()))
        lst = list(map(lambda x:x-1,lst))
        x.append(lst)
    priority.append(x)

for i in range(1000):
    move()
    if check():
        print(i+1)
        exit(0)
    # for row in board:
    #     print(row)
    # print()
print(-1)


