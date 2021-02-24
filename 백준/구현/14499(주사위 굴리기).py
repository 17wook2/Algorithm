n,m,x,y,k = list(map(int,input().split()))
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
move = list(map(int,input().split()))

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

# 상하좌우 4개
dice = [0] * 4
top = 0
bottom = 0

# 주사위를 상하로 굴리면 좌우는 고정되고, 좌우로 굴리면 상하는 고정된다는 것이 핵심
def changeDice(direction):
    global top
    global bottom
    temp1 = top
    temp2 = bottom
    if direction == 1:
        # 2는 좌 3은 우
        bottom = dice[3]
        top = dice[2]
        dice[2] = temp2
        dice[3] = temp1
    elif direction == 2: # 왼쪽으로 굴릴때
        # 2는 좌 3은 우
        bottom = dice[2]
        top = dice[3]
        dice[3] = temp2
        dice[2] = temp1
    elif direction == 3: # 위로 굴릴때
        bottom = dice[0]
        top = dice[1]
        dice[0] = temp1
        dice[1] = temp2
    elif direction == 4:
        bottom = dice[1]
        top = dice[0]
        dice[0] = temp2
        dice[1] = temp1

def start(x,y):
    global top
    global bottom
    for direction in move:
        # 이동 가능한지 확인
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < m:
            changeDice(direction)
            x,y = nx,ny
            if array[nx][ny] == 0:
                array[nx][ny] = bottom
            else:
                bottom = array[nx][ny]
                array[nx][ny] = 0
        else:
            continue
        print(top)

start(x,y)