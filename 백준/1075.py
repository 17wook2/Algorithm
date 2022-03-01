n = int(input())
f = int(input())
s = str(n)
ans = ''
for i in range(100):
    s = str(n)
    s = s[0:len(s)-2]
    x = str(i).zfill(2)
    s = s + x
    t = int(s)
    if t % f == 0:
        ans = x
        break
print(ans)