a,b = map(int,input().split())
arr = [0] * (b-a+1)
i = 2
ans = b-a+1
while i*i <= b:
    k = i*i
    remain = 0 if a % k == 0 else 1
    j = a // k + remain
    while k*j <= b:
        if not arr[k*j-a]:
            arr[k*j-a] = 1
            ans -= 1
        j += 1
    i += 1
print(ans)