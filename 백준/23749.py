from collections import deque
n = int(input())
arr = list(input().split())
tmp = ''.join(arr)
ans = 999
queue = deque([])
queue.append(('',0,0))
def iswin(a):
    rtn = 0
    for i in range(0,2*n,2):
        if a[i:i+2] == 'OX':
            rtn += 1
        elif a[i:i+2] == 'XO':
            rtn -= 1
    return rtn
def comp(a,b):
    x = len(a)
    rtn = 0
    flag = False
    if iswin(a) <= 0:
        return 9999
    for i in range(x):
        if a[i] != b[i] and not flag:
            rtn += 1
            flag = True
        else:
            flag = False
    return rtn

while queue:
    batch,o,x = queue.popleft()
    if len(batch) == 2*n:
        rtn = comp(batch,tmp)
        ans = min(rtn,ans)
    else:
        if o < n:
            batch += 'O'
            queue.append((batch,o+1,x))
            batch = batch[:-1]
        if x < n:
            batch += 'X'
            queue.append((batch,o,x+1))
print(ans)
