import math
n,p = map(int,input().split())
arr = list(map(int,input().split()))
ans = math.inf
for k in range(p,n+1):
    avg = sum(arr[0:k])/k
    var = 0
    for i in range(k):
        var += (arr[i]-avg)**2
    var /= k
    ans = min(ans,var)
    for i in range(n-k):
        new_avg = avg - (arr[i]/k) + (arr[i+k]/k)
        new_var = 0
        for j in range(1,k+1):
            new_var += abs(arr[i+j]-new_avg)**2
        new_var /= k
        ans = min(ans,new_var)
        avg = new_avg
print(math.sqrt(ans))
