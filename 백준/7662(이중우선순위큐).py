import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    sheap = []
    mheap = []
    visited = [0]*1000000
    count = 0
    for i in range(n):
        a,b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(sheap,(b,i)) # 최소 힙 구성
            heapq.heappush(mheap,(-b,i)) # max힙 구성
        # 동기화를 해주어야함.
        elif a == 'D':
            if b == -1:
                while sheap and visited[sheap[0][1]]:
                    heapq.heappop(sheap)
                if sheap:
                    x,t = heapq.heappop(sheap)
                    visited[t] = 1
            else:
                while mheap and visited[mheap[0][1]]:
                    heapq.heappop(mheap)
                if mheap:
                    x, t = heapq.heappop(mheap)
                    visited[t] = 1

    while sheap and visited[sheap[0][1]]:
        heapq.heappop(sheap)
    while mheap and visited[mheap[0][1]]:
        heapq.heappop(mheap)
    if mheap and sheap:
        print(-mheap[0][0], sheap[0][0])
    else:
        print('EMPTY')


