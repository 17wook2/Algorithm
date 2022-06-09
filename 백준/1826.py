import heapq
n = int(input())
stations = []
heap = []
for i in range(n):
    a,b = map(int,input().split())
    stations.append([a,b])
stations.sort(key = lambda x:x[0])
v = list(map(int,input().split()))
start = v[1]
end = v[0]
idx = 0
ans = 0
while start < end:
    while idx < n and stations[idx][0] <= start:
        a,b = stations[idx]
        heapq.heappush(heap,-b)
        idx += 1
    if heap:
        b = heapq.heappop(heap)
        start += -b
        ans += 1
    else:
        ans = -1
        break
print(ans)



