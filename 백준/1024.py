n,l = map(int,input().split())
ans = -1
ansl = 0
for i in range(l,101):
    b = i*(i-1) // 2
    if (n-b) >= 0 and (n-b) % i == 0:
        x = (n-b) // i
        ans = x
        ansl = i
        break
if ans == -1:
    print(-1)
else:
    for x in range(ans,ans+ansl):
        print(x, end=' ')

