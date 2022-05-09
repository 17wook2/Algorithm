import sys
sys.setrecursionlimit(10**5)
s = int(input())
ans = sys.maxsize
dp = [[-1]*1001 for i in range(1001)]
def dfs(cnt,board):
   if cnt > 1000 or cnt < 1 or board > 1000:
       return sys.maxsize
   if cnt == s:
       return 0
   if dp[cnt][board] != -1:
       return dp[cnt][board]
   dp[cnt][board] = sys.maxsize
   dp[cnt][board] = min(dp[cnt][board], dfs(cnt,cnt) + 1)
   dp[cnt][board] = min(dp[cnt][board], dfs(cnt+board,board) +1)
   dp[cnt][board] = min(dp[cnt][board], dfs(cnt-1,board) + 1)
   return dp[cnt][board]
print(dfs(1,0))
