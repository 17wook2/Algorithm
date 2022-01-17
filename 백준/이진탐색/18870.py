n = int(input())
a = list(map(int,input().split()))

b = a[:]
b.sort()
c = []
for e in b:
    if len(c) == 0:
        c.append(e)
    elif c[-1] != e:
        c.append(e)
    else:
        continue

def lowerbound(target):
    st = 0
    en = len(c)
    while st < en:
        mid = (st + en) // 2
        if c[mid] < target:
            st = mid + 1
        else:
            en = mid
    return st

def upperbound(target):
    st = 0
    en = len(c)
    while st<en:
        mid = (st + en) // 2
        if c[mid] < target:
            st = mid + 1
        else:
            en = mid
    return st



for e in a:
    print(lowerbound(e),end=' ')
