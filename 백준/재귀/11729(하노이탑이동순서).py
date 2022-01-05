n = int(input())
# k개를 이동한다고 하면
# 1~k-1개를 1 -> 2로
# k를 1 -> 3으로
# 1~k-1개를 2-> 3으로

def func(a,b,k): # k개를 a-> b로 이동시키는 함수
    if k==1:
        print(f"{a} {b}")
        return
    func(a,6-a-b,k-1)
    print(f"{a} {b}")
    func(6-a-b,b,k-1)

print((1<<n)-1)
func(1,3,n)