n,s = list(map(int,input().split()))
arr = list(map(int,input().split()))
ans = 0
def go(cnt,cost):
    global ans
    if cnt == n:
        if cost == s:
            ans += 1
        return
    go(cnt+1,cost)
    go(cnt+1,cost+arr[cnt])
go(0,0)

if s == 0:
    ans -= 1
print(ans)