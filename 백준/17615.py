n = int(input())
arr = list(input())
ans = n
def go(color,direction):
    check = 0; cnt = 0
    if direction == 0:
        for i in range(n):
            if arr[i] != color: check = 1
            elif arr[i] == color and check: cnt += 1
    elif direction == 1:
        for i in range(n-1,-1,-1):
            if arr[i] != color: check = 1
            elif arr[i] == color and check: cnt += 1
    return cnt
for color in ['R','B']:
    for direciton in [0,1]:
        ans = min(ans,go(color,direciton))
print(ans)