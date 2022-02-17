mx = 1200005
pre = [-1] * mx
nxt = [-1] * mx
def solution(n, k, cmds):
    s = ['O'] * n
    for i in range(n):
        pre[i], nxt[i] = i - 1, i + 1
    nxt[n - 1] = -1
    cursor = k
    erased = []
    for cmd in cmds:
        q = cmd.split(" ")
        if q[0] == 'U':
            for i in range(int(q[1])):
                cursor = pre[cursor]
        elif q[0] == 'D':
            for i in range(int(q[1])):
                cursor = nxt[cursor]
        elif q[0] == 'C':
            erased.append((pre[cursor], cursor, nxt[cursor]))
            if pre[cursor] != -1: nxt[pre[cursor]] = nxt[cursor]
            if nxt[cursor] != -1: pre[nxt[cursor]] = pre[cursor]
            s[cursor] = 'X'
            if nxt[cursor] != -1:
                cursor = nxt[cursor]
            else:
                cursor = pre[cursor]
        elif q[0] == 'Z':
            p, c, n = erased.pop()
            if p != -1: nxt[p] = c
            if n != -1: pre[n] = c
            s[c] = 'O'

    return ''.join(s)


