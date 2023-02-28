n = int(input())
arr = []
for i in range(n):
    x,y = list(map(int,input().split()))
    arr.append((x,y))
arr.sort(key = lambda x:x[0])
top_x,top_y = 0,0
for i in range(n):
    x,y = arr[i]
    if y > top_y:
        top_x = i; top_y = y
ans = 0
idx = 0
left = []
while idx <= top_x:
    x,y = arr[idx]
    if len(left) > 0:
        cur_x,cur_y = left[-1]
        if y >= cur_y: left.append((x,y))
    else: left.append((x,y))
    idx += 1
for i in range(len(left)-1):
    ans += (left[i+1][0]-left[i][0])*left[i][1]
ans += top_y
idx = n-1
right = []
while idx >= top_x:
    x,y = arr[idx]
    if len(right) > 0:
        cur_x,cur_y = right[-1]
        if y >= cur_y: right.append((x,y))
    else: right.append((x,y))
    idx -= 1
for i in range(len(right)-1):
    ans += (right[i][0] - right[i+1][0])*right[i][1]

print(ans)




