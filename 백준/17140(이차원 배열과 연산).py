r,c,k = list(map(int,input().split()))
a = []
for i in range(3):
    a.append(list(map(int,input().split())))

def checkoperator(a): ## R연산이면 True C연산이면 False
    row = len(a)
    col = len(a[0])
    if row >= col:
        return True
    else:
        return False

def sorting(board):
    rtn = []
    cnt = 0
    for row in board:
        d = {}
        for e in row:
            if e == 0:
                continue
            if e in d:
                d[e] += 1
            else:
                d[e] = 1
        t = list(zip(d.keys(),d.values()))
        t.sort(key = lambda x:(x[1], x[0]))
        if len(t) >= 100:
            t = t[0:100]
        tmp = []
        for x in t:
            tmp.append(x[0])
            tmp.append(x[1])
        cnt = max(cnt, len(tmp))
        rtn.append(tmp)
    for i in range(len(rtn)):
        while len(rtn[i]) != cnt:
            rtn[i].append(0)
    return rtn

time = 0
while time <= 100:
    if len(a) >= r and len(a[0]) >= c:
        if a[r-1][c-1] == k:
            break

    if checkoperator(a): ## R연산인경우
        a = sorting(a)
    else:
        a = list(map(list,zip(*a)))
        a = sorting(a)
        a = list(map(list,zip(*a)))
    time += 1

if time == 101:
    time = -1
print(time)
