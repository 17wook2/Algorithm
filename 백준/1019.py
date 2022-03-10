n = int(input())
ans = [0]*10
p = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            ans[int(i)] += p
        n -= 1
    if n < 10:
        for i in range(n+1):
            ans[i] += p
        ans[0] -= p
        break
    else:
        for i in range(10):
            ans[i] += (n//10 + 1)*p
    ans[0] -= p
    n //= 10
    p *= 10
print(*ans)