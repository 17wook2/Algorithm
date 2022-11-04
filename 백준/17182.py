import math
n,k = list(map(int,input().split()))
dist = []
for i in range(n):
    dist.append(list(map(int,input().split())))
for p in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][p] + dist[p][j]:
                dist[i][j] = dist[i][p] + dist[p][j]
ans = math.inf
end = (1<<n) - 1
def func(visited,start,cost):
    global ans
    if visited == end:
        ans = min(ans,cost)
        return
    for node in range(n):
        if not visited & (1 << node): ## 해당 노드를 방문하지 않았다면
            new = visited | (1 << node)
            surcost = dist[start][node]
            func(new,node, cost + surcost)

func(end&(1<<k),k,0)
print(ans)

