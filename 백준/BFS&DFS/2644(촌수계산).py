from collections import deque
n = int(input())
a,b = list(map(int,input().split()))
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    p,c = list(map(int,input().split()))
    graph[p].append(c)
    graph[c].append(p)
# print(graph)
def bfs(start,end):
    count = [-1] * (n+1)
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                count[i] = count[v] + 1
    # print(count)
    return count[end]+1 if count[end] != -1 else -1
print(bfs(a,b))


