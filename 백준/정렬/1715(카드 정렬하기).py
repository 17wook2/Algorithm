import heapq
n = int(input())
numbers = []
for i in range(n):
    heapq.heappush(numbers,int(input()))
if n == 1:
    print(0)
else:
    answer = 0
    while len(numbers) >= 2:
        a = heapq.heappop(numbers)
        b = heapq.heappop(numbers)
        answer += a
        answer += b
        heapq.heappush(numbers,a+b)
    print(answer)

