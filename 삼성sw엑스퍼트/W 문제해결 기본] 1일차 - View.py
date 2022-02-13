for _ in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(2,n-2):
        a = arr[i-2]
        b = arr[i-1]
        c = arr[i+1]
        d = arr[i+2]
        if max(a,b,c,d) >= arr[i]:
            continue
        l = max(a,b)
        r = max(c,d)
        ans += min(arr[i]-l,arr[i]-r)
    print(f"#{_+1} {ans}")