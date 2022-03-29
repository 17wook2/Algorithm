from collections import deque
lst = list(map(int,input().split()))
lst.sort()
a,b,c = lst
s = sum(lst)
if s % 3 != 0:
    print(0)
else:
    x = s // 3
    visited = [[0]*1501 for i in range(1501)]
    queue = deque([])
    queue.append((a,b))
    ans = 0
    while queue:
        a,b = queue.popleft()
        lst = [a,b,s-a-b]
        lst.sort()
        a,b,c = lst
        if a == x and b == x:
            ans = 1
            break
        visited[a][b] = 1
        visited[a][c] = 1
        visited[b][c] = 1
        if not visited[a+a][b-a]:
            visited[a+a][b-a] = 1
            queue.append((a+a,b-a))
        if not visited[a+a][c-a]:
            visited[a+a][c-a] = 1
            queue.append((a+a,c-a))
        if not visited[b+b][c-b]:
            visited[b+b][c-b] = 1
            queue.append((b+b,c-b))
    print(ans)


