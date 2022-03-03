n,k = map(int,input().split())
ans = 0
while True:
    count = bin(n).count('1')
    if count > k:
        idx = bin(n)[::-1].index('1')
        ans += 2**idx
        n += 2**idx
    else:
        break
print(ans)
