n = int(input())
arr = list(map(int,input().split()))
m = int(input())
left = 0; right = max(arr) + 1
def check(mid):
    p_sum = 0
    for i in range(n):
        if arr[i] <= mid: p_sum += arr[i]
        else: p_sum += mid
    if p_sum <= m: return True
    else: return False

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid): left = mid
    else: right = mid
print(left)

