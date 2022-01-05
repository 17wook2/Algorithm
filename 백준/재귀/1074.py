n,r,c = list(map(int,input().split()))

def func(a,b,k):
    if k == 0:
        return 0
    half = 1 << (k-1)
    if a < half and b < half:
        return func(a,b,k-1)
    if a< half and b >= half:
        return half*half + func(a,b-half,k-1)
    if a >= half and b < half:
        return 2*half*half + func(a-half,b,k-1)
    return 3*half*half + func(a-half,b-half,k-1)

print(func(r,c,n))
