mx = 1200005
data = [-1] * mx
pre = [-1] * mx
nxt = [-1] * mx
unused = 1
num2idx = [-1] * mx
def insert(address, num):
    global unused
    data[unused] = num
    pre[unused] = address
    nxt[unused] = nxt[address]
    if nxt[address] != -1:
        pre[nxt[address]] = unused
    nxt[address] = unused
    unused += 1
    return unused - 1
def erase(address):
    nxt[pre[address]] = nxt[address]
    if nxt[address] != -1:
        pre[nxt[address]] = pre[address]
        return nxt[address]
    return pre[address]
def solution(n, k, cmd):
    for i in range(n):
        num2idx[i] = insert(i, i)
    cursor = num2idx[k]
    stack = []
    for cm in cmd:
        a = cm.split(" ")
        if a[0] == 'D':
            for i in range(int(a[1])):
                cursor = nxt[cursor]
        elif a[0] == 'U':
            for i in range(int(a[1])):
                cursor = pre[cursor]
        elif a[0] == 'C':
            stack.append((data[pre[cursor]], data[cursor]))
            cursor = erase(cursor)
        elif a[0] == 'Z':
            a, b = stack.pop()
            if a == -1:
                preidx = 0
            else:
                preidx = num2idx[a]
            num2idx[b] = insert(preidx, b)

    s = ['X'] * n
    cur = nxt[0]
    while cur != -1:
        s[data[cur]] = 'O'
        cur = nxt[cur]
    return ''.join(s)


