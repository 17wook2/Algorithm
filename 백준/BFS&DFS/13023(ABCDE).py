import sys
n,m = map(int,input().split())
graph = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
def dfs(start, visited, deps):
    if deps >= 4:
        return True
    for v in graph[start]:
        if not visited[v]:
            visited[v] = 1
            if dfs(v,visited,deps + 1) == True:
                return True
            visited[v] = 0


def check():
    for i in range(n):
        visited = [0]*n
        visited[i] = 1
        if dfs(i,visited,0) == 1:
            return True
    return False


print(1 if check() else 0)

