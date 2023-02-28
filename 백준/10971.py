import math
n = int(input())
graph = []
for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
visited = [0]*n
ans = math.inf
def go(start,cost,cnt):
    global ans
    if cnt == n-1:
        if graph[start][0] != 0:
            ans = min(ans,cost+graph[start][0])
        return
    for i in range(n):
        if i == 0: continue
        if visited[i]: continue
        if graph[start][i] == 0: continue
        visited[i] = 1
        go(i,cost + graph[start][i],cnt+1)
        visited[i] = 0

go(0,0,0)
print(ans)