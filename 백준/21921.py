n,x = map(int,input().split())
arr = list(map(int,input().split()))
p_sum = sum(arr[:x])
max_visit = p_sum
cnt = 1
for i in range(n-x):
    p_sum -= arr[i]
    p_sum += arr[i+x]
    if p_sum > max_visit:
        max_visit = p_sum
        cnt = 1
    elif p_sum == max_visit:
        cnt += 1
if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)



