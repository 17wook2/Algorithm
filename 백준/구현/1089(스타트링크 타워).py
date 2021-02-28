n = int(input())
sign = []
for i in range(5):
    sign.append(input())
nums = [set() for _ in range(10)]
nums[0] = {0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14}
nums[1] = {2, 5, 8, 11, 14}
nums[2] = {0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14}
nums[3] = {0, 1, 2, 5, 6, 7, 8, 11, 12, 13, 14}
nums[4] = {0, 2, 3, 5, 6, 7, 8, 11, 14}
nums[5] = {0, 1, 2, 3, 6, 7, 8, 11, 12, 13, 14}
nums[6] = {0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14}
nums[7] = {0, 1, 2, 5, 8, 11, 14}
nums[8] = {0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14}
nums[9] = {0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14}

def check(array):
    temp = set()
    pos = []
    for i in range(5):
        for j in range(3):
            if array[i][j] == '#':
                temp.add(i*3+j)
    for k in range(10):
        if nums[k].intersection(temp) == temp:
            pos.append(k)
    return pos

def sol():
    possible = []
    for i in range(n):
        array = [row[i * 4:i * 4 + 3] for row in sign]
        possible.append(check(array))
    total_branch = 1
    for row in possible:
        total_branch *= len(row)
    summation = 0
    # print(possible)
    for i, row in enumerate(possible):
        for col in row:
            # print(col*(10**(len(possible)-i-1)))
            summation += col * (10 ** (len(possible) - i - 1)) * total_branch // len(row)
            # print(summation)
    if total_branch != 0:
        print(summation / total_branch)
    else:
        print(-1)
sol()
