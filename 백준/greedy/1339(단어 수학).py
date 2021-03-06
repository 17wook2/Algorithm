n = int(input())
words = []
priority = {}
for i in range(n):
    words.append(input())
for word in words:
    l = len(word) - 1
    for idx,e in enumerate(word):
        if e in priority:
            priority[e] += pow(10,l-idx)
        else:
            priority[e] = pow(10,l-idx)
# print(priority)
digit = []
for v in priority.values():
    digit.append(v)
digit.sort(reverse=True)
k = 9
answer = 0
for d in digit:
    answer += d * k
    k -= 1
print(answer)