import heapq
n = int(input())
arr = []
heap = []
parent = [-1]*(n+1)
ans = 0
cnt = 0
def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b
def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]
for i in range(n):
    arr.append([i]+list(map(int,input().split())))
for i in range(1,4):
    arr.sort(key = lambda x:x[i])
    for j in range(len(arr)-1):
        dist = abs(arr[j][i] - arr[j+1][i])
        heapq.heappush(heap,(dist,arr[j][0],arr[j+1][0]))
while heap:
    dist,x,y = heapq.heappop(heap)
    if find(x) != find(y):
        cnt += 1
        ans += dist
        union(x,y)
    if cnt == n-1:
        break
print(ans)