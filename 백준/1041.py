n = int(input())
arr = list(map(int,input().split()))
lst = []
lst.append(min(arr[0],arr[5]))
lst.append(min(arr[1],arr[4]))
lst.append(min(arr[2],arr[3]))
lst.sort()
dim1_min = lst[0]
dim2_min = lst[0] + lst[1]
dim3_min = lst[0] + lst[1] + lst[2]

if n == 1:
    print(sum(arr)-max(arr))
else:
    default = 4*dim3_min + 4*dim2_min
    if n > 2:
        default += (n-2)*(n-2)*dim1_min
        default += 4*(n-1)*(n-2)*dim1_min
        default += 8*(n-2)*dim2_min
    print(default)