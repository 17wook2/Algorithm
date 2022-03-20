n,k = map(int,input().split())
nlist = list(str(n))
length = len(nlist)
dp = [[-1]*11 for i in range(1000010)]
def dfs(node,depth):
    if depth == k:
        return int(node)
    if dp[int(node)][depth] != -1:
        return dp[int(node)][depth]
    for i in range(length-1):
        for j in range(i+1,length):
            tolist = list(node)
            if i == 0 and tolist[j] == '0':
                continue
            tolist[i], tolist[j] = tolist[j], tolist[i]
            tostr = ''.join(tolist)
            dp[int(node)][depth] = max(dp[int(node)][depth], dfs(tostr,depth+1))
            tolist[i], tolist[j] = tolist[j], tolist[i]
    return dp[int(node)][depth]

print(dfs(str(n),0))
