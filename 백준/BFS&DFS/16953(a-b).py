from collections import deque
a,b = list(map(int,input().split()))
deq = deque([])
deq.append((a,1))
res = -1
while deq:
    # print(deq)
    now,count = deq.popleft()
    if now == b:
        res = count
        break
    if now*2 <= b:
        deq.append((now*2,count+1))
    if int(str(now)+'1') <= b:
        deq.append((int(str(now)+'1'),count+1))
print(res)