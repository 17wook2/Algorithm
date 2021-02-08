import heapq
T = int(input())
for _ in range(T):
    n = int(input())
    files = list(map(int,input().split()))
    heap = []
    answer = 0
    for file in files:
        heapq.heappush(heap,file)
    while heap:
        if len(heap) <= 1:
            break;
        else:
            temp1 = heapq.heappop(heap)
            temp2 = heapq.heappop(heap)
            # print(temp1 + temp2)
            answer += temp1
            answer += temp2
            heapq.heappush(heap,temp1 + temp2)
    print(answer)
