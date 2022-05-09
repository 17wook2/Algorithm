t = int(input())
for i in range(t):
    m,n,x,y = list(map(int,input().split()))
    ans = -1
    k = x
    while k <= m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            ans = k
            break
        k += m
    print(ans)