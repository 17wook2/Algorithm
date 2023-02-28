n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input())))
ans = []
for k in range(1<<(n*m)):
    total = 0
    for i in range(n):
        rowsum = 0
        for j in range(m):
            idx = m*i + j
            if (1 << idx) & k:
                rowsum = rowsum * 10 + arr[i][j]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum

    for j in range(m):
        colsum = 0
        for i in range(n):
            idx = i*m + j
            if not (1 << idx) & k:
                colsum = colsum * 10 + arr[i][j]
            else:
                total += colsum
                colsum = 0
        total += colsum
    ans.append(total)

print(max(ans))