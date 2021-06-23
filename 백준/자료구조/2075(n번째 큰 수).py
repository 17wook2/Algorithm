import heapq
n = int(input())
heap = []
for i in range(n):
    a = list(map(int,input().split()))
    if i == 0:
        for e in a:
            heapq.heappush(heap,e)
    else:
        for e in a:
            if heap[0] > e:
                continue
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,e)
count = len(heap) - n
while not count:
    answer = heapq.heappop(heap)
    count -= 1
print(answer)

