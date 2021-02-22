n = int(input())
k = int(input())
board = [[0]*(n+1) for i in range(n+1)]
for i in range(k):
    a,b = list(map(int,input().split()))
    board[a][b] = 1
l = int(input())
rotate = []
for i in range(l):
    x,c = list(input().split())
    rotate.append((int(x),c))
dx = [0,1,0,-1] # 동 남 서 북
dy = [1,0,-1,0]
def rotation(direction,c):
    if c == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

def solution():
    x,y = 1,1
    time = 0
    direction = 0
    idx = 0
    stack = [(x,y)]
    board[x][y] = 2
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2: # 벽 아니거나 자기 꼬리 아닐때
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                stack.append((nx,ny))
            else:
                board[nx][ny] = 2
                stack.append((nx,ny))
                a,b = stack.pop(0)
                board[a][b] = 0
        else:
            time += 1
            break
        x, y = nx, ny #머리 위치 바꾸기
        time += 1
        if idx < l and rotate[idx][0] == time:
            direction = rotation(direction, rotate[idx][1])
            idx += 1
    return time
print(solution())



