from collections import deque
n,m = list(map(int,input().split()))
field = [list((input())) for _ in range(m)] # n은 가로 m은 세로
# print(field)
def bfs(color):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    deq = deque([])
    visited = [[0]*n for i in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 1 or field[i][j] != color: # 방문 했거나 아군이 아니면
                continue
            elif visited[i][j] == 0 and field[i][j] == color:
                deq.append((i,j))
                ally = 0
                while deq:
                    x,y = deq.popleft()
                    visited[x][y] = 1
                    ally += 1
                    for k in range(4):   # 이동
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<= nx <m and 0<=ny<n and not visited[nx][ny] and field[nx][ny] == color: #인덱스 범위 안, 방문 안했고, 아군이면
                            # print(nx,ny)
                            deq.append((nx,ny))
                            visited[nx][ny] = 1
                        else:
                            continue
                count += ally * ally
    return count
print(bfs('W'),bfs('B'))



