import math
import heapq

def dijkstra(start,limit):

    distance = [math.inf]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cur_dist, cur_des = heapq.heappop(q)
        if distance[cur_des] < cur_dist:
            continue

        for node in graph[cur_des]:
            if node[1] > limit:
                if cur_dist + 1 < distance[node[0]]:
                    distance[node[0]] = cur_dist + 1
                    heapq.heappush(q, (cur_dist + 1, node[0]))
            else:
                if cur_dist < distance[node[0]]:
                    distance[node[0]] = cur_dist
                    heapq.heappush(q, (cur_dist, node[0]))
    if distance[n] > k:
        return False
    else:
        return True

n,p,k = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
for i in range(p):
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))

lo, ro = -1, 1000001
ans = math.inf
while lo + 1 < ro:
    mid = (lo + ro) // 2
    res = dijkstra(1,mid)
    if res:
        ro = mid
        ans = ro
    else:
        lo = mid
if ans == math.inf:
    print(-1)
else:
    print(ans)