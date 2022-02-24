from itertools import combinations
import heapq
n,c = list(map(int,input().split()))
def getDistance(ax,ay,bx,by):
    r1 = abs(ax-bx)
    r2 = abs(ay-by)
    return r1**2 + r2**2
def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

locations = []
for i in range(n):
    locations.append(list(map(int,input().split())))

cases = list(combinations(range(n),2))
parent = [i for i in range(n)]
heap = []
for case in cases:
    dist = getDistance(locations[case[0]][0],locations[case[0]][1],locations[case[1]][0],locations[case[1]][1])
    if dist >= c:
        heapq.heappush(heap,(dist,case))
cnt = 0
ans = 0
while len(heap) > 0 and cnt < n-1:
    dist,case = heapq.heappop(heap)
    if find(case[0]) != find(case[1]):
        cnt += 1
        ans += dist
        union(case[0],case[1])

ans = -1 if cnt != n-1 else ans
print(ans)
