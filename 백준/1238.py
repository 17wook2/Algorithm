import heapq
import math
def dijkstra(start, distance, array):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        weight, idx = heapq.heappop(q)
        for node in array[idx]:
            cur_des = node[0]
            cur_dist = node[1]
            if distance[cur_des] > weight + cur_dist:
                distance[cur_des] = weight + cur_dist
                heapq.heappush(q, (distance[cur_des], cur_des))


n,m,x = list(map(int,input().split()))
arr = [[] for i in range(n+1)]
revArr = [[] for i in range(n+1)]
dist = [math.inf]*(n+1)
revDist = [math.inf]*(n+1)

for i in range(m):
    u,v,w = list(map(int,input().split()))
    arr[u].append((v,w))
    revArr[v].append((u,w))

dijkstra(x,dist,arr)
dijkstra(x,revDist,revArr)
ans = -1
for i in range(1,n+1):
    ans = max(ans,dist[i] + revDist[i])
print(ans)



