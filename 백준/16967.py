h,w,x,y = list(map(int,input().split()))
b = []
for i in range(h+x):
    b.append(list(map(int,input().split())))
for i in range(x,h):
    for j in range(y,w):
        b[i][j] -= b[i-x][j-y]

for i in range(h):
    print(*b[i][:w])