n,m = list(map(int,input().split()))
before = []
after = []
ans = 0
for i in range(n):
    before.append(list(map(int,input())))
for i in range(n):
    after.append(list(map(int,input())))

def toggle(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if before[i][j] == 0:
                before[i][j] = 1
            else:
                before[i][j] = 0

for i in range(n-2):
    for j in range(m-2):
        if before[i][j] != after[i][j]:
            toggle(i,j)
            ans += 1

for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            ans = -1
print(ans)
