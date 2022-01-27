n,k = list(map(int,input().split()))
board = []
horses = []
board2 = [[[]*n for i in range(n)] for i in range(n)]
ans = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
horses.append([0,0,0])
for i in range(k):
    horse = list(map(int,input().split()))
    horse[0] -= 1
    horse[1] -= 1
    horse[2] -= 1
    board2[horse[0]][horse[1]].append(i+1)
    horses.append(horse)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(hidx):
    x,y,d = horses[hidx] ## idx에 해당하는 말 꺼내기
    nx = x + dx[d]
    ny = y + dy[d]
    if not 0 <= nx < n or not 0<= ny < n or board[nx][ny] == 2: ## 나가거나 파란색일때
        if d < 2:
            d = (d+1) % 2
        else:
            d = (d+1) % 2
            d += 2
        nx = x + dx[d] ## 방향 바꾸기
        ny = y + dy[d]
        horses[hidx][2] = d ## 말 배열 update
        if not 0 <= nx < n or not 0<= ny < n or board[nx][ny] == 2: ##방향 바꾸고 이동해도 파란색이면
            return 0
    ## 한칸 이동
    idx = board2[x][y].index(hidx)  ## 이동 전 칸에서 말 인덱스 찾기
    s = board2[x][y][idx:]
    board2[x][y] = board2[x][y][:idx]  ## 이동 전칸 변경
    if board[nx][ny] == 1: ## 빨간색이면
        s.reverse()
    board2[nx][ny].extend(s)
    for i in board2[nx][ny]:
        horses[i][0] = nx
        horses[i][1] = ny

    if len(board2[nx][ny]) >= 4: ## 게임 종료
        return 1

while ans < 1000:
    ans += 1
    for i in range(1,k+1):
        if move(i):
            print(ans)
            exit(0)
print(-1)



