import math
import heapq
def dijkstra():
    q = [(arr[0][0],0,0)]
    dist[0][0] = arr[0][0]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        w,x,y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                    dist[nx][ny] = dist[x][y] + arr[nx][ny]
                    heapq.heappush(q,(dist[nx][ny],nx,ny))
    return dist[n-1][n-1]


arr = []
dist = []
cnt = 0
while True:
    n = int(input())
    cnt += 1
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    dist = [[math.inf]*n for i in range(n)]
    res = dijkstra()
    print(f"Problem {cnt}: {res}")