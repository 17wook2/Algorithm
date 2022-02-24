import heapq
n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap,list(map(int,input().split())))
cur_time = 0
while len(heap) > 0:
    st,wt = heapq.heappop(heap)
    if st >= cur_time:
        cur_time = st
    cur_time += wt
print(cur_time)