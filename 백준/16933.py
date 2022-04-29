from collections import deque
import sys
input = sys.stdin.readline
n,m,k = list(map(int,input().split()))
arr = []
dx = [-1,0,1,0]; dy = [0,1,0,-1]
for i in range(n):
    arr.append(list(map(int,input().strip())))
visited = [[[0]*(k+1) for i in range(m+1)] for i in range(n+1)] ## n/m/k
visited[0][0] = [1]*(k+1)
queue = deque([])
queue.append((0,0,0))
def bfs():
    day = 1
    cnt = 0
    while queue:
        q = len(queue)
        cnt += 1
        for _ in range(q):
            x,y,nk = queue.popleft()
            if x == n-1 and y == m-1:
                return cnt
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1 and nk < k and not visited[nx][ny][nk+1]: ## 부술 수 있고 낮이면
                        if day:
                            queue.append((nx,ny,nk+1))
                            visited[nx][ny][nk+1] = 1
                        else:
                            queue.append((x, y, nk))
                    if arr[nx][ny] == 0 and not visited[nx][ny][nk]:
                        visited[nx][ny][nk] = 1
                        queue.append((nx,ny,nk))
        day ^= 1
    return -1
print(bfs())