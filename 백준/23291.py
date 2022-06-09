from collections import deque
n,k = map(int,input().split())
arr = [[0]*n for i in range(n-1)]
arr.append(list(map(int,input().split())))

def add():
    x = min(arr[n-1])
    for i in range(n):
        if arr[n-1][i] == x:
            arr[n-1][i] += 1

def roll():
    idx = 1; cnt = 0; w = 1; h = 1
    while True:
        if idx + h > n:
            break
        queue = deque([])
        for i in range(w):
            for j in range(h):
                queue.append(arr[n-1-j][idx-(w-i)])
                arr[n-1-j][idx-(w-i)] = 0
        for i in range(w):
            for j in range(h):
                arr[n-1-(w-i)][idx+j] = queue.popleft()
        if cnt % 2 == 1:
            w += 1
        else:
            h += 1
        idx += w
        cnt += 1
    # print(idx,h)
    # for row in arr:
    #     print(row)
    # print()
def control():
    global arr
    queue = deque([])
    queue.append((n-1,n-1))
    mapping = [[0]*n for i in range(n)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0:
                mapping[x][y] += arr[x][y]
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0:
                        if arr[x][y] > arr[nx][ny]:
                            d = (arr[x][y] - arr[nx][ny]) // 5
                            mapping[x][y] -= d
                            mapping[nx][ny] += d
    arr = mapping

def relocate():
    idx = 0
    for i in range(n):
        for j in range(n-1,-1,-1):
            if arr[j][i] == 0:
                break
            arr[n-1][idx] = arr[j][i]
            if j < n-1:
                arr[j][i] = 0
            idx += 1

def fold():
    k = n
    k //= 2
    stack = []
    for i in range(k):
        stack.append(arr[n-1][i])
        arr[n-1][i] = 0
    for i in range(k,n):
        arr[n-2][i] = stack.pop()
    k //= 2
    for i in range(2*k,3*k):
        stack.append(arr[n-2][i])
        arr[n-2][i] = 0
    for i in range(2*k,3*k):
        stack.append(arr[n-1][i])
        arr[n-1][i] = 0
    for i in range(2,0,-1):
        for j in range(3*k,n):
            arr[n-2-i][j] = stack.pop()
def result():
    t = max(arr[n-1])
    v = min(arr[n-1])
    if t - v <= k:
        return True
    else:
        return False
def clean():
    while True:
        global ans
        add()
        roll()
        control()
        relocate()
        fold()
        control()
        relocate()
        if result():
            return
        else:
            ans += 1
ans = 1
clean()
print(ans)