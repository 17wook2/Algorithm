N = int(input())
meets = []
for i in range(N):
    meets.append(list(map(int,input().split())))
meets.sort(key = lambda x: x[0])
meets.sort(key = lambda x: x[1])
time = 0
answer = 0
# print(meets)
for meet in meets:
    if time <= meet[0]:
        time = meet[1]
        answer += 1
    else:
        continue
print(answer)
