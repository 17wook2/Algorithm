t = int(input())
for _ in range(t):
    ans = 0
    n = int(input())
    arr = list(map(int,input().split()))
    idx = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        if arr[i] <= arr[idx]: ## 체크한 인덱스 값
            continue
        else:
            cnt = idx - i - 1
            temp_sum = sum(arr[i+1:idx])
            ans += (arr[idx] * cnt - temp_sum)
            idx = i
    temp_sum = sum(arr[0:idx])
    cnt = idx
    ans += (arr[idx] * cnt - temp_sum)
    print(f"#{_+1} {ans}")


