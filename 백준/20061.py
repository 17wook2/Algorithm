n = int(input())
green = [[0]*4 for i in range(10)]
blue =  [[0]*4 for i in range(10)]
score = 0
block = 0
def setting(array,loc):
    for l in loc:
        x,y = l
        array[x][y] = 1

def move(array):
    blocks = []
    for i in range(4):
        for j in range(4):
            if array[i][j] == 1:
                blocks.append([i,j])
                array[i][j] = 0
    blocks.sort(key = lambda x:x[0], reverse=True)
    h = 10
    for i in range(len(blocks)):
        idx = 0
        x,y = blocks[i]
        while x + idx < 10 and array[x+idx][y] == 0:
            idx += 1
        h = min(h,idx)
    for i in range(len(blocks)):
        array[blocks[i][0]+h-1][blocks[i][1]] = 1

def erase(array,row,cnt):
    for i in range(cnt):
        for j in range(4):
            array[row-i][j] = 0
    for i in range(row-cnt,3,-1):
        for j in range(4):
            array[i+cnt][j] = array[i][j]
            array[i][j] = 0
def check(array):
    check_list = []
    cnt = 0
    for i in range(9,5,-1):
        if sum(array[i]) == 4:
            check_list.append(i)
    check_list.sort()
    for x in check_list:
        erase(array,x,1)
    if sum(array[5]) > 0:
        cnt += 1
    if sum(array[4]) > 0:
        cnt += 1
    if cnt > 0:
        erase(array,9,cnt)

    return len(check_list)

def count(array):
    cnt = 0
    for i in range(9,5,-1):
        for j in range(4):
            if array[i][j] == 1:
                cnt += 1
    return cnt
for i in range(n):
    t,x,y = list(map(int,input().split()))
    loc = [[x,y]]
    if t == 2:
        loc.append([x,y+1])
    elif t == 3:
        loc.append([x+1,y])
    setting(green,loc)
    for i in range(len(loc)):
        loc[i][0],loc[i][1] = loc[i][1], 3-loc[i][0]
    setting(blue,loc)
    move(green)
    move(blue)
    score += check(green)
    score += check(blue)
block += count(green)
block += count(blue)

print(score)
print(block)