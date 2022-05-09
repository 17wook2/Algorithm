n = input()
digit = len(n)
number = int(n)
ans = 0
for i in range(digit-1,-1,-1):
    x = number - 10**i + 1
    ans += x*(i+1)
    number = 10**i - 1
print(ans)
