import sys
from collections import deque
def bfs(x,y):
    queue = deque([])
    queue.append((x,y))
    vision[x][y] = '.'
    tmp = board[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and vision[nx][ny] == '#' and board[nx][ny] == tmp:
                vision[nx][ny] = '.'
                queue.append((nx,ny))
def move(x):
    global hr,hc
    if x == 'W':
        bfs(hr,hc)
    elif x == 'U':
        hr -= 1
    elif x == 'R':
        hc += 1
    elif x == 'D':
        hr += 1
    elif x == 'L':
        hc -= 1

r,c = map(int,sys.stdin.readline().split())
board = []
for i in range(r):
    x = list(sys.stdin.readline())
    board.append(x)

hr,hc = list(map(int,input().split()))
hr -= 1
hc -= 1
vision = [['#']*c for i in range(r)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
order_list = sys.stdin.readline()
for order in order_list:
    move(order)

vision[hr][hc] = '.'
for i in range(4):
    nx = hr + dx[i]
    ny = hc + dy[i]
    if 0 <= nx < r and 0 <= ny < c:
        vision[nx][ny] = '.'

for row in vision:
    print("".join(row))
# print(vision)