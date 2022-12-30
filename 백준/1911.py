n,l = map(int,input().split())
arr = []
for i in range(n):
    s,e = map(int,input().split())
    arr.append((s,e))
arr.sort()
pos = 0
ans = 0
for s,e in arr:
    if pos < s:
        cnt = (e-s)//l
        if (e-s)%l != 0:
            cnt += 1
        pos = s + l * cnt
        ans += cnt
    elif s <= pos <= e:
        cnt = (e-pos) // l
        if (e-pos) % l != 0:
            cnt += 1
        pos += l * cnt
        ans += cnt
    elif pos > e:
        continue
print(ans)
