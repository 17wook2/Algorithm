import math
t = int(input())
dp = [math.inf]*101
dp[2]= 1; dp[3] = 7; dp[4] = 4; dp[5] = 2; dp[6] = 6; dp[7] = 8; dp[8] = 10;
nums = [0,0,1,7,4,2,0,8];
def getMin(value):
    for i in range(9,101):
        for j in range(2,8):
            dp[i] = min(dp[i], dp[i-j]*10 + nums[j])

def getMax(value):
    s = ''
    while value:
        if value % 2 != 0:
            s += '7'
            value -= 3
        else:
            s += '1'
            value -= 2
    return s
for i in range(t):
    value = int(input())
    getMin(value)
    print(dp[value], getMax(value))