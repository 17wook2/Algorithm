a,b = list(map(int,input().split()))
dp = [0]*60
for i in range(1,60):
    dp[i] = 2**(i-1) + 2*dp[i-1]
def go(x):
    cnt = 0
    binary = bin(x)[2:]
    length = len(binary)
    for i in range(length):
        if binary[i] == '1':
            pow = length -i-1
            cnt += dp[pow]
            cnt += (x - 2**pow +1)
            x = x - 2**pow
    return cnt

print(go(b) - go(a-1))

