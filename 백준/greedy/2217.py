n = int(input())
jul = []
for i in range(n):
    jul.append(int(input()))
jul.sort()
ans = 0
for i in range(1,n+1):
    ans = max(ans, jul[n-i]*i)
print(ans)