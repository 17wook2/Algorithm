import sys,heapq
n = int(sys.stdin.readline())
maxheap = []
minheap = []
ans = []
for i in range(n):
    number = int(sys.stdin.readline())
    if len(maxheap) == len(minheap): # 크기가 같다면 maxheap에
        heapq.heappush(maxheap,(-number,number))
    else:
        heapq.heappush(minheap,(number,number))
    if minheap and maxheap[0][1] > minheap[0][1]:
        temp_max = heapq.heappop(maxheap)[1]
        temp_min = heapq.heappop(minheap)[1]
        heapq.heappush(maxheap,(-temp_min,temp_min))
        heapq.heappush(minheap,(temp_max,temp_max))
    ans.append(maxheap[0][1])
for a in ans:
    print(a)
