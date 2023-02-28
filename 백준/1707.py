from collections import deque
k = int(input())
def bfs(x):
    q = deque()
    q.append((x,1))
    while q:
        x,group = q.popleft()
        visited[x] = group
        for node in graph[x]:
            if not visited[node]:
                visited[node] = -1 * group
                q.append((node,-1*group))
            else:
                if visited[x] == visited[node]:
                    return False
    return True

for _ in range(k):
    v,e = list(map(int,input().split()))
    graph = [[] for i in range(v+1)]
    visited = [0]*(v+1)
    ans = 'YES'
    for i in range(e):
        a,b = list(map(int,input().split()))
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if not visited[i]:
            if not bfs(i):
                ans = 'NO'
                break
    print(ans)
