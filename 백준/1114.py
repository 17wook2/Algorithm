l,k,c = list(map(int,input().split()))
arr = [0,l] + list(map(int,input().split()))
arr.sort()
def check(x): ## 가장 긴 조각이 x 보다 작아질 수 있을까? => 모든 자른거가 길이가 x보다 작아야함
    cnt = 0
    pos = l
    cutted = []
    for i in range(len(arr) - 1, -1, -1):
        dist = arr[i] - arr[i - 1]
        total = pos - arr[i]
        if dist > x:
            return 10001,-1
        elif total > x:
            pos = arr[i + 1]
            cutted.append(arr[i + 1])
            cnt += 1
    if cnt < c: return cnt, arr[1]
    else: return cnt, cutted[-1]

def go():
    start = 0
    end = l
    a,b = 0,0
    while start + 1 < end:
        mid = (start + end) // 2
        cnt, pos = check(mid)
        if cnt > c:
            start = mid
        else:
            a = cnt; b = pos
            end = mid
    print(end,b)
go()