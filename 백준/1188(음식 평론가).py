n,m = map(int,input().split())
for i in range(m,m*(n+1),m):
    if i % n == 0:
        length = i
        break
print(length)
# 개별 소시지 길이
a = length // n
b = length // m
c = (a//b) - 1
print(c*n)