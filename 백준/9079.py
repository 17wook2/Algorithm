from collections import deque
t = int(input())
## [2,2] = 0 부터 [0,0] = 8
curs = [[8,7,6],[5,4,3],[2,1,0],[8,5,2],[7,4,1],[6,3,0],[8,4,0],[6,4,2]]
def go(start):
    q = deque([(start,0)])
    visited[start] = 1
    while q:
        x,cnt = q.popleft()
        if x == 0 or x == idx: return cnt
        for cur in curs:
            nx = x
            for i in cur:
                nx ^= (1<<i)
            if not visited[nx]:
                visited[nx] = 1
                q.append((nx,cnt+1))
    return -1
for _ in range(t):
    idx = (1<<9) - 1
    visited = [0 for i in range(1<<9)]
    start = ''
    for i in range(3):
        row = list(input().split())
        for j in range(3):
            if row[j] == 'H': start += '1'
            else: start += '0'
    start = int(start,2)
    res = go(start)
    print(res)
