n,m,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
def check(x): ## 심판과 심판 사이의 거리가 x보다 크게 배치할 때 m명을 배치할 수 있을지 검증
    cnt = 0; pos = -1
    for i in range(k):
        if pos <= arr[i]:
            cnt += 1
            pos = arr[i] + x
    if cnt < m: return False
    else: return True

def search():
    start = 0; end = arr[-1]+1
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid): start = mid
        else: end = mid
    return start

def go():
    ans = ''
    pos = -1; cnt = 0
    for i in range(k):
        if pos <= arr[i] and cnt < m:
            ans += '1'
            pos = arr[i] + dist
            cnt += 1
        else:
            ans += '0'
    print(ans)
dist = search()
go()
