x,y = map(int,input().split())
z = (y*100) // x
if z >= 99:
    print(-1)
else:
    left = 0
    right = 1000000000
    answer = 0
    while left < right:
        mid = (left + right) // 2
        if (y+mid)*100 // (x+mid) >= z+1:
            right = mid
        else:
            left = mid + 1
    print(left)
