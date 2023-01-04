from collections import deque
n, k = map(int,input().split())
q = deque()
visited = [0]*100001
check = [0]*100001
q.append(n)
def move(x):
    stream = []
    pos = x
    for i in range(visited[x] + 1):
        stream.append(pos)
        pos = check[pos]
    return ' '.join(map(str, stream[::-1]))

while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        print(move(x))
        break
    for next in [x-1,x+1,2*x]:
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = visited[x] + 1
            q.append(next)
            check[next] = x
