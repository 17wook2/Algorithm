while True:
    n,a,b = list(map(int,input().split()))
    if n == 0 and a == 0 and b == 0:
        break
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    arr.sort(key = lambda x : abs(x[1]-x[2]),reverse= True)
    ans = 0
    temp = []
    for i in range(n):
        k,da,db = arr[i]
        x = 0
        if da <= db:
            x = min(k,a)
            ans += da*x
            ans += db*(k-x)
            a -= x; b -= (k-x)
        elif da > db:
            x = min(k,b)
            ans += da*(k-x)
            ans += db*x
            a -= (k-x); b -= x
        else:
            temp.append([k,da,db])
    print(ans)
