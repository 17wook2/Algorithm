def solve(cnt,ops):
    if cnt == n-1:
        temp = ''
        v = ''
        for i in range(1,n+1):
            temp += str(i); v+= str(i)
            if i <= n - 1:
                if ops[i-1] != ' ': temp += ops[i-1]
                v += ops[i-1]
        if eval(temp) == 0:
            case.append(v)
        return
    for op in [' ','+','-']:
        ops.append(op)
        solve(cnt+1,ops)
        ops.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    case = []
    solve(0,[])
    for c in case:
        print(c)
    print()