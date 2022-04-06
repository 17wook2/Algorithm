import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n+1)]
depth = [-1]*(n+1)
parent = [0]*(n+1)
def dfs(x,cnt):
    depth[x] = cnt
    for node in graph[x]:
        if depth[node] == -1:
            parent[node] = x
            dfs(node,cnt+1)
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1,0)
m = int(input())
for _ in range(m):
    u,v = map(int,input().split())
    while depth[u] != depth[v]:
        if depth[u] > depth[v]:
            u = parent[u]
        else:
            v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    print(u)


