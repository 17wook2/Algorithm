r,c,t = list(map(int,input().split()))
board = []
for i in range(r):
    board.append(list(map(int,input().split())))
s = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r):
    if board[i][0] == -1:
        s = i
        break

def diffusion():
    temp = []
    for i in range(r):
        for j in range(c):
            if board[i][j] >= 5:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        cnt += 1
                        temp.append((nx,ny,board[i][j] // 5))
                board[i][j] -= (board[i][j]//5) * cnt
    for t in temp:
        board[t[0]][t[1]] += t[2]

def clean():
    for i in range(s):
        board[s-i][0] = board[s-i-1][0]
    # print(board)
    for i in range(1,r-s-1):
        board[s+i][0] = board[s+i+1][0]
    # print(board)

    for i in range(c-1):
        board[0][i] = board[0][i+1]
        board[r-1][i] = board[r-1][i+1]

    for i in range(s):
        board[i][c-1] = board[i+1][c-1]
    for i in range(1,r-s-1):
        board[r-i][c-1] = board[r-i-1][c-1]

    for i in range(1,c-1):
        board[s][c-i] = board[s][c-i-1]
        board[s+1][c-i] = board[s+1][c-i-1]

    board[s][1] = 0
    board[s+1][1] = 0
    board[s][0] = -1
    board[s+1][0] = -1

for i in range(t):
    diffusion()
    clean()

answer = 0
for row in board:
    answer += sum(row)

answer += 2

print(answer)