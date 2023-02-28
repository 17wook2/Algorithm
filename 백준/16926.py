n,m,r = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
def go():
    for i in range(min(n,m)//2):
        x,y = i,i
        temp = arr[x][y]
        for j in range(i+1,n-i):
            x = j
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
        for j in range(i+1,m-i):
            y = j
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
        for j in range(i+1,n-i):
            x = n-j-1
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev
        for j in range(i+1,m-i):
            y = m-j-1
            prev = arr[x][y]
            arr[x][y] = temp
            temp = prev

for i in range(r):
    go()

for row in arr:
    print(*row)