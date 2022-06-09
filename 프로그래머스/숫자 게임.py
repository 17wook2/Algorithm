import heapq
def solution(a,b):
    idx = 0
    a.sort()
    heapq.heapify(b)
    while b:
        x = heapq.heappop(b)
        if a[idx] >= x:
            continue
        elif a[idx] < x:
            idx += 1
    return idx