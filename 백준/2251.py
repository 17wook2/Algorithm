from collections import deque
def move(x,y):
    if not vis[x][y]:
        vis[x][y] = 1
        q.append((x,y))
def bfs():
    while q:
        x,y = q.popleft()
        z = c-x-y
        if x == 0:
            ans.append(z)
        water = min(x,b-y)
        move(x - water, y + water)
        water = min(x,c-z)
        move(x - water, y)
        water = min(y,a-x)
        move(x + water, y - water)
        water = min(y,c-z)
        move(x,y-water)
        water = min(z,a-x)
        move(x+water, y)
        water = min(z,b-y)
        move(x,y + water)

a,b,c = list(map(int,input().split()))
vis = [[0]*(b+1) for i in range(a+1)]
vis[0][0] = 1
q = deque()
q.append((0,0))
ans = []
bfs()
ans.sort()
print(*ans)
