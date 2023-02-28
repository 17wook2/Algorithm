from collections import deque
n = int(input())
q = deque([i for i in range(1,n+1)])
while q:
    x = q.popleft()
    if len(q) == 0:
        print(x)
        break
    x = q.popleft()
    q.append(x)

