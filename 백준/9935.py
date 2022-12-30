a = input()
b = input()
stack = []
for x in a:
    stack.append(x)
    if x == b[-1] and ''.join(stack[-len(b):]) == b:
        for i in range(len(b)):
            stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))