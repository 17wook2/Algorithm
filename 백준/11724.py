n,m = list(map(int,input().split()))
visited = [0]*(n+1)
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
def go(x):
    visited[x] = 1
    for node in graph[x]:
        if not visited[node]:
            go(node)
for i in range(1,n+1):
    if not visited[i]:
        cnt += 1
        go(i)
print(cnt)

