n = int(input())
arr = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

arr.sort()
def lowerbound(target):
    st = 0
    en = n
    while st < en:
        mid = (st + en) // 2
        if arr[mid] < target:
            st = mid + 1
        else:
            en = mid
    return st

def upperbound(target):
    st = 0
    en = n
    while st < en:
        mid = (st+en) // 2
        if arr[mid] <= target:
            st = mid + 1
        else:
            en = mid
    return st

for e in b:
    lb = lowerbound(e)
    ub = upperbound(e)
    print(ub-lb)
