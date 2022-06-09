t = int(input())
for test_cse in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = list(map(lambda x:x%2, arr))
    odd = 0
    even = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if abs(odd-even) >= 2:
        print(f"#{test_cse} -1")
        continue
    visited = [0]*(n+1)
    cnt = 0
    for i in range(n-1):
        if arr[i] == arr[i+1] and not visited[i]:
            cnt += 1
            visited[i+1] = 1
    print(f"#{test_cse} {(cnt // 2) + (cnt%2)}")


