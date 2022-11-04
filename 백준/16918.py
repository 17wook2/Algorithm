def simulate(n):
    while n > 0:
        set_bomb()
        n -= 1
        if n == 0:
            return
        burst()
        n -= 1
        if n == 0:
            return
    return

def burst():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    temp = []
    for i in range(r):
        for j in range(c):
            if time[i][j] == 1:
                array[i][j] = '.'
                temp.append((i,j))
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if time[nx][ny] == 1:
                        array[i][j] = '.'
                        time[i][j] = 0
    for location in temp:
        x,y = location
        time[x][y] = 0


def set_bomb():
    for i in range(r):
        for j in range(c):
            if array[i][j] == '.':
                time[i][j] = 2
                array[i][j] = 'O'
            elif array[i][j] == 'O':
                time[i][j] -= 1

r,c,n = list(map(int,input().split()))
array = []
for i in range(r):
    array.append(list(input()))

time = [[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        if array[i][j] == 'O':
            time[i][j] = 2

n -= 1
simulate(n)
for i in range(r):
    for j in range(c):
        print(array[i][j],end='')
    print()




