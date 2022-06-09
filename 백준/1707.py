import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
k = int(input())
def dfs(start):
    global check
    for node in graph[start]:
        if visited[node] == 0:
            visited[node] = -visited[start]
            dfs(node)
        elif visited[node] == visited[start]:
            check = False
            return
for _ in range(k):
    v,e = map(int,input().split())
    visited =[0]*(v+1)
    graph = [[] for i in range(v+1)]
    ans = 'YES'
    check = True
    for i in range(e):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,v+1):
        if not visited[i]:
            visited[i] = 1
            dfs(i)
            if not check:
                ans = 'NO'
                break
    print(ans)
