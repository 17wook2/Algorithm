n = int(input())
u = []
for i in range(n):
    u.append(int(input()))
u.sort()
ans = 0
tu = []
for i in range(n):
    for j in range(i,n):
        tu.append(u[i]+u[j])
tu.sort()

def bs(target):
    st = 0
    en = len(tu)-1
    while st <= en:
        mid = (st + en) // 2
        if tu[mid] == target:
            return 1
        elif tu[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return None
for i in range(n-1,-1,-1):
    for j in range(i):
        x = u[i]-u[j]
        if bs(x):
            print(u[i])
            exit(0)

