import heapq
v,e = map(int,input().split())
heap = []
parent = [-1]*(v+1)
ans = 0
def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(u,v):
    if u < v:
        parent[u] += parent[v]
        parent[v] = u
    else:
        parent[v] += parent[u]
        parent[u] = v
for i in range(e):
    a,b,c = list(map(int,input().split()))
    heapq.heappush(heap,(c,a,b))
while heap:
    c,a,b = heapq.heappop(heap)
    a = find(a)
    b = find(b)
    if a != b:
        union(a,b)
        ans += c
print(ans)