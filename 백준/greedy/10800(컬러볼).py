import sys
input = sys.stdin.readline
n = int(input())
balls = []
for i in range(n):
    balls.append(list(map(int,input().split())))
    balls[i].append(i+1)
balls.sort(key = lambda x:(x[1],x[0]))
# print(balls)
dp = [0] * (n+1)
answer = [0] * (n+1)
acc = 0
j = 0
for i in range(n):
    a = balls[i]
    b = balls[j]
    while b[1] < a[1]: # 색갈 다른데 크기 같은거 나오면 같은거 끝날때가지 더해줌
        acc += b[1]
        dp[b[0]] += b[1]
        j += 1
        b = balls[j]
    answer[a[2]] = acc - dp[a[0]]
for i in range(1,len(answer)):
    print(answer[i])