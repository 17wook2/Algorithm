from collections import deque
def go():
    ans = 0
    while True:
        visited = bfs()
        if not check(visited):
            break
        ans += 1
        bomb(visited)
        move()
    return ans

def bomb(visited):
    bomb_array = [0]*70
    for i in range(12):
        for j in range(6):
            if visited[i][j] != 0:
                bomb_array[visited[i][j]] += 1
    t = []
    for i in range(1,70):
        if bomb_array[i] >= 4: t.append(i)
    for i in range(12):
        for j in range(6):
            if visited[i][j] in t:
                arr[i][j] = '.'

def move():
    for i in range(6):
        s = []
        for j in range(11,-1,-1):
            if arr[j][i] != '.':
                s.append(arr[j][i])
                arr[j][i] = '.'
        for j in range(len(s)):
            arr[11-j][i] = s[j]

def check(visited):
    bomb_array = [0] * 70
    for i in range(12):
        for j in range(6):
            if visited[i][j] != 0:
                bomb_array[visited[i][j]] += 1
    t = []
    for i in range(1, 70):
        if bomb_array[i] >= 4: t.append(i)
    if len(t) > 0:
        return True
    else:
        return False


def bfs():
    cnt = 0
    visited = [[0]*6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visited[i][j]:
                cnt += 1
                q = deque([])
                q.append((i,j))
                visited[i][j] = cnt
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                            visited[nx][ny] = visited[x][y]
                            q.append((nx,ny))
    return visited


dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = []
for i in range(12):
    arr.append(list(input()))
print(go())