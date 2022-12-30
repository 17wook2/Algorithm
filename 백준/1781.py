import heapq
n = int(input())
arr = []
for i in range(n):
    a,b = list(map(int,input().split()))
    arr.append((a,b))
arr.sort()
q = []
for a,b in arr:
    heapq.heappush(q,b)
    if a < len(q):
        heapq.heappop(q)
print(sum(q))