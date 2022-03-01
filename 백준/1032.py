n = int(input())
word_dict = []
for i in range(n):
    word_dict.append(input())
ans = ''
for i in range(len(word_dict[0])):
    start = word_dict[0][i]
    ans += start
    for j in range(len(word_dict)):
        if word_dict[j][i] != start:
            ans = ans[:-1]
            ans += '?'
            break
print(ans)