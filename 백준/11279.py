import heapq
lst = []
n = int(input())
answer = []
for i in range(n):
    number = int(input())
    if number == 0:
        try:
            answer.append(heapq.heappop(lst)[1])
        except:
            answer.append(0)
            continue
    else:
        heapq.heappush(lst,(abs(number),number))
for ans in answer:
    print(ans)