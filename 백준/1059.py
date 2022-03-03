import bisect
l = int(input())
arr = list(map(int,input().split()))
n = int(input())
arr.sort()
idx = bisect.bisect_left(arr,n)
left = arr[idx-1]
right = arr[idx]
if left == n or right == n:
    print(0)
else:
    if idx == 0:
        left = 0
        right = arr[idx]
    a = left + 1
    b = right - 1
    p = (n-a+1)*(b-n+1)
    p -= 1
    print(p)

