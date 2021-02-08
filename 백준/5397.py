from collections import deque
T = int(input())
for i in range(T):
    left = []
    right = []
    L = input().rstrip()
    for i in L:
        if i == '<':
            if len(right) != 0:
                left.append(right.pop())
        elif i == '>':
            if len(left) != 0:
                right.append(left.pop())
        elif i == '-':
            if len(right) != 0:
                right.pop()
        else:
            right.append(i)
    left.reverse()
    # print(right, left)
    right = right + left
    print(''.join(right))
