from collections import deque
n = int(input())
graph = [[0]*n for i in range(n)]
for i in range(n):
    lst = list(input())
    for j in range(len(lst)):
        if lst[j] == 'N':
            continue
        else:
            graph[i][j] = 1

def bfs(idx):
    count = 0
    visited = [0]*n
    queue = deque([])
    queue.append((idx,0))
    while queue:
        t,depth = queue.popleft()
        visited[t] = 1
        if depth >= 2:
            continue
        for i in range(n):
            if not visited[i] and graph[t][i] == 1:
                visited[i] = 1
                count += 1
                queue.append((i,depth+1))
    return count
ans = 0
for i in range(n):
    ans = max(ans,bfs(i))
print(ans)
