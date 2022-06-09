n = int(input())
arr = list(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
d = 2
x,y = 0,0
q = [[0,0]]
for a in arr:
    if a == 'F':
        x = x + dx[d]
        y = y + dy[d]
        q.append([x,y])
        continue
    if a == 'L':
        d -= 1
    elif a == 'R':
        d += 1
    d = (d+4) % 4
max_x = 0
min_x = 99
min_y = 99
max_y = 0
for i in q:
    min_x = min(min_x, i[0])
    min_y = min(min_y, i[1])
for i in range(len(q)):
    q[i][0] -= min_x
    q[i][1] -= min_y
    max_x = max(max_x, q[i][0])
    max_y = max(max_y, q[i][1])

arr = [['#']*(max_y+1) for i in range(max_x+1)]
for i in q:
    x,y = i
    arr[x][y] = '.'
for row in arr:
    print(*row, sep='')
