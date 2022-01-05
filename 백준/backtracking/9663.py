n = int(input())
visited = [0]*n
cnt = 0
isused = [0]*40
isused2 = [0]*40
isused3 = [0]*40
def func(k):
    global cnt
    if k == n:
        cnt+=1
    for i in range(n):
        if isused[i] or isused2[i+k] or isused3[k-i+1]:
            continue
        isused[i] = 1
        isused2[i+k] = 1
        isused3[k-i+1] = 1
        func(k+1)
        isused[i] = 0
        isused2[i+k] = 0
        isused3[k-i+1] = 0

func(0)
print(cnt)
