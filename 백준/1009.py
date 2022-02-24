t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    k = a
    for i in range(b-1):
        k *= a
        k %= 10
    k = k % 10
    if k == 0:
        print(10)
    else:
       print(k)
