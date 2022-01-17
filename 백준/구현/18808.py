n,m,k = list(map(int,input().split()))
stickers = []
for i in range(k):
    x,y = list(map(int,input().split()))
    sticker = []
    for i in range(x):
        sticker.append(list(map(int,input().split())))
    stickers.append(sticker)

book = [[0]*m for i in range(n)]

def attach(x,y,sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] + book[i+x][j+y] == 2:
                return False
    return True

def check(sticker):
    x = len(sticker)
    y = len(sticker[0])
    if x > n or y > m:
        return False
    for i in range(n-x+1):
        for j in range(m-y+1):
            if attach(i,j,sticker): # 붙일수 있는경우
                for a in range(x):
                    for b in range(y):
                        book[i+a][j+b] += sticker[a][b]
                return True
    return False

def rotate_90(sticker):
    x = len(sticker)
    y = len(sticker[0])
    ret = [[0]*x for i in range(y)]

    for r in range(y):
        for c in range(x):
            ret[r][c] = sticker[x-c-1][r]
    return ret

for i in range(len(stickers)):
    for j in range(4):
        if check(stickers[i]): ## 붙일 수 있는경우
            break
        else:
            stickers[i] = rotate_90(stickers[i])

cnt = 0
for row in book:
    cnt += row.count(1)
print(cnt)
