k = input()
a_cnt = k.count('a')
ans = 1001
for i in range(len(k)):
    sub = ''
    if i + a_cnt >= len(k):
        comp = (i + a_cnt) % len(k)
        sub = k[i:len(k)] + k[0:comp]
    else:
        sub = k[i:i+a_cnt]
    b_cnt = sub.count('b')
    ans = min(ans,b_cnt)
print(ans)
