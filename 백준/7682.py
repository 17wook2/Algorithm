def check(array):
    x,y = 0,0
    for i in range(3):
        if array[i][0] == array[i][1] and array[i][1] == array[i][2]:
            if array[i][0] == 'X':
                x = 1
            elif array[i][0] == 'O':
                y = 1
        if array[0][i] == array[1][i] and array[1][i] == array[2][i]:
            if array[0][i] == 'X':
                x = 1
            elif array[0][i] == 'O':
                y = 1
    if array[0][0] == array[1][1] and array[1][1] == array[2][2]:
        if array[0][0] == 'X':
            x = 1
        elif array[0][0] == 'O':
            y = 1
    if array[0][2] == array[1][1] and array[1][1] == array[2][0]:
        if array[0][2] == 'X':
            x = 1
        elif array[0][2] == 'O':
            y = 1
    return (x,y)
while True:
    arr = input()
    if arr == 'end':
        break
    else:
        graph = [[] for i in range(3)]
        x = []
        o = []
        for i in range(3):
            for j in range(3):
                if arr[i*3 + j] == 'X':
                    x.append((i,j))
                elif arr[i*3 + j] == 'O':
                    o.append((i,j))
                graph[i].append(arr[i*3+j])
        lx = len(x)
        lo = len(o)
        if lx < lo or lx - lo >= 2:
            print("invalid")
            continue
        l,r = check(graph)
        if l == 0 and r == 0:
            if lx == 5 and lo == 4:
                print("valid")
            else:
                print("invalid")
        if l == 1 and r == 0:
            if lx - lo == 1:
                print("valid")
            else:
                print("invalid")
        if l == 0 and r == 1:
            if lx == lo:
                print("valid")
            else:
                print("invalid")
        if l == 1 and r == 1:
            print("invalid")
