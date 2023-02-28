n = int(input())
a = [0]*26
cnt = 0
t = input()
for e in t:
    a[ord(e)-65] += 1
for i in range(n-1):
    b = [0]*26
    x = input()
    for e in x:
        b[ord(e)-65] += 1
    diff = 0
    for i in range(26):
        diff += abs(a[i] - b[i])
    if sum(a) == sum(b) and diff <= 2:
        cnt += 1
    elif sum(a) != sum(b) and diff <= 1:
        cnt += 1
print(cnt)