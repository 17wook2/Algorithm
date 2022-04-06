import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
L = 21
n = int(input())
graph = [[] for i in range(n+1)]
parent = [[0]*L for i in range(n+1)]
d = [-1]*(n+1)
def dfs(x,cnt):
    d[x] = cnt
    for node in graph[x]:
        if d[node] == -1:
            parent[node][0] = x
            dfs(node,cnt+1)
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1,0)
for j in range(1,L):
    for i in range(1,n+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]
m = int(input())
for _ in range(m):
    u,v = map(int,input().split())
    if d[u] > d[v]:
        u,v = v,u
    for i in range(L-1,-1,-1):
        if d[v]-d[u] >= (1<<i):
            v = parent[v][i]
    if u == v:
        print(u)
        continue
    for i in range(L-1,-1,-1):
       if parent[u][i] != parent[v][i]:
           u = parent[u][i]
           v = parent[v][i]
    print(parent[u][0])
