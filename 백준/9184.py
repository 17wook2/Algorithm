while True:
    a,b,c = list(map(int,input().split()))
    if a == -1 and b == -1 and c == -1: break
    dp = [[[0]*21 for i in range(21)] for i in range(21)]
    dp[0][0][0] = 1
    def go(a,b,c):
        if a <= 0 or b <= 0 or c <= 0: return 1
        if a > 20 or b > 20 or c > 20: return go(20,20,20)
        if dp[a][b][c]: return dp[a][b][c]
        if a < b and b < c:
                dp[a][b][c] = go(a,b,c-1) + go(a,b-1,c-1) - go(a,b-1,c)
                return dp[a][b][c]
        else:
            dp[a][b][c] = go(a-1,b,c) + go(a-1,b-1,c) + go(a-1,b,c-1) - go(a-1,b-1,c-1)
            return dp[a][b][c]
    ans = go(a,b,c)
    print(f"w({a}, {b}, {c}) = {ans}")