import sys
n,m = list(map(int,sys.stdin.readline().split()))
book = {}
cnt = 0
for i in range(n):
    word = sys.stdin.readline().rstrip()
    book[word] = 1
for i in range(m):
    words = list(sys.stdin.readline().rstrip().split(","))
    for word in words:
        if word in book and book[word] == 1:
            cnt += 1
            book[word] = 0
    print(n-cnt)