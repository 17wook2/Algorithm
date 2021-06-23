from collections import deque
n,m,v = list(map(int,input().split()))
graph = [[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    x,y = list(map(int,input().split()))
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (n+1)
def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1,n+1):
        if (visited[i] == 0 and graph[v][i] == 1):
            dfs(i)

def bfs():
    queue = deque([v])
    while queue:
        k = queue.popleft()
        visited[k] = 1
        print(k, end= ' ')
        for i in range(1,n+1):
            if not visited[i] and graph[k][i] == 1:
                queue.append(i)
                visited[i] = 1


dfs(v)
print()
visited = [0]*(n+1)
bfs()