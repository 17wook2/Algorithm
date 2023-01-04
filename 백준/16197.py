n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
pos = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            pos.append((i,j))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = float('inf')
def oob(x,y):
    if x < 0 or x >= n or y < 0 or y >= m: return 1
    return 0
def check(x,y):
    if 0 <= x < n and 0 <= y < m and arr[x][y] == '#': return True
    return False
def go(cnt,ax,ay,bx,by):
    global ans
    if cnt > 10: return
    for i in range(4):
        nax = ax + dx[i]
        nay = ay + dy[i]
        nbx = bx + dx[i]
        nby = by + dy[i]
        if oob(nax,nay) ^ oob(nbx,nby) and cnt < 10:
            ans = min(ans,cnt+1)
            continue
        if oob(nax, nay) and oob(nbx, nby): continue
        if check(nax,nay): nax = ax; nay = ay
        if check(nbx,nby): nbx = bx; nby = by
        go(cnt+1,nax,nay,nbx,nby)

go(0,pos[0][0],pos[0][1],pos[1][0],pos[1][1])
if ans == float('inf'):
    ans = -1
print(ans)



