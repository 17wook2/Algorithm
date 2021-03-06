n = int(input())
numbers = list(map(int,input().split()))
stack = []
dp = [0] * (n)
for i in range(len(numbers)):
    try:
        while numbers[stack[-1]] < numbers[i]:
            k = stack.pop()
        dp[i] = stack[-1] + 1
        stack.append(i)
    except:
        dp[i] = 0
        stack.append(i)
print(*dp)

