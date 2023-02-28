n = int(input())
m = int(input())
if m > 0:
    arr = list(map(int,input().split()))
ans = abs(n-100)
try:
    for i in range(1000001):
        nums = str(i)
        for j in range(len(nums)):
            if int(nums[j]) in arr:
                break
            elif j == len(nums) - 1:
                ans = min(ans,abs(i-n)+len(nums))
    print(ans)
except NameError:
    print(min(abs(100-n),len(str(n))))
