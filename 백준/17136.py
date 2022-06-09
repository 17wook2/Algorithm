arr = []
for i in range(10):
    arr.append(list(map(int,input().split())))
ans = 99
def check(x,y,n,array):
    if x + n > 10 or y + n > 10:
        return False
    for i in range(n):
        for j in range(n):
            if array[x+i][y+j]:
                continue
            else:
                return False
    return True

def toggle(x,y,n,array):
    for i in range(n):
        for j in range(n):
            array[x+i][y+j] ^= 1

def isfilled(array):
    ans = 0
    for row in array:
        ans += sum(row)
    if ans == 0:
        return True
    else:
        return False

def dfs(x,y,cnt,array):
    y %= 10
    if x >= 10:
        return
    global ans
    for c in cnt:
        if c > 5:
            return
    if array[x][y]:
        for k in range(5,0,-1):
            if cnt[k-1] > 5 or sum(cnt) >= ans:
                continue
            if check(x,y,k,array):
                toggle(x,y,k,array)
                cnt[k-1] += 1
                dfs(x,y+k,cnt,array)
                toggle(x,y,k,array)
                cnt[k-1] -= 1
    else:
        if y == 9:
            dfs(x+1,0,cnt,array)
        else:
            dfs(x,y+1,cnt,array)
    if isfilled(array):
        ans = min(ans,sum(cnt))

dfs(0,0,[0,0,0,0,0],arr)

if ans == 99:
    print(-1)
else:
    print(ans)