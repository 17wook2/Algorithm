from collections import deque
left = deque(input())
right = deque()
m = int(input())
for i in range(m):
    order = list(input())
    if order[0] == 'P':
        word = order[2]
        left.append(word)
    elif order[0] == 'L':
        if len(left) != 0: right.appendleft(left.pop())
    elif order[0] == 'D':
        if len(right) != 0: left.append(right.popleft())
    elif order[0] == 'B':
        if len(left) != 0: left.pop()
left.extend(right)
print(''.join(left))