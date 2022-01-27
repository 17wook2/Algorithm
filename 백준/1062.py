n,k = list(map(int,input().split()))
words = []
ans = 0
for i in range(n):
    words.append(input())

if k < 5:
    print(0)
    exit(0)
if k == 26:
    print(n)
    exit(0)

study = [0] * 26
for alphabet in ['a','n','t','i','c']:
    study[ord(alphabet) - ord('a')] = 1

def dfs(idx, cnt):
    global ans
    if cnt == k - 5:
        word_count = 0
        for word in words:
            for alphabet in word:
                if not study[ord(alphabet) - ord('a')]:
                    break;
            else:
                word_count += 1

        ans = max(ans,word_count)
        return

    for i in range(idx,26):
        if not study[i]:
            study[i] = 1
            dfs(i,cnt+1)
            study[i] = 0

dfs(0,0)

print(ans)

