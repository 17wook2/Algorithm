n,d,k,c = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(int(input()))
arr.extend(arr)
check = [0]*(d+1)
check[c] = 1
cnt = 1
for i in range(k):
    if not check[arr[i]]:
        cnt += 1
    check[arr[i]] += 1
ans = cnt
for i in range(2*n-k):
    check[arr[i]] -= 1
    if not check[arr[i]]:
        cnt -= 1
    if not check[arr[i+k]]:
        cnt += 1
    check[arr[i+k]] += 1
    ans = max(ans,cnt)
print(ans)
