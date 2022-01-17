n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()
for e in b:
    st = 0
    en = n-1
    while st<=en:
        mid = (st+en) // 2
        if a[mid] < e:
            st = mid + 1
        elif a[mid] > e:
            en = mid - 1
        else:
            print(1)
            break
    if st > en:
        print(0)
