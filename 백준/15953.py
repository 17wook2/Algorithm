t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    x = 6
    px = [0,500,300,200,50,30,10]
    y = 5
    ans = 0
    for i in range(1,x+1):
        if a == 0 or a > 21:
            break
        if a - i > 0:
            a -= i
        else:
            ans += px[i]
            break
    for i in range(y+1):
        if b == 0 or b > 31:
            break
        if b - (1<<i) > 0:
            b -= (1<<i)
        else:
            ans += 512>>i
            break
    print(ans*10000)


