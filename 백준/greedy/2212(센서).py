n = int(input())
k = int(input())
numbers = list(map(int,input().split()))
numbers = list(set(numbers))
numbers.sort()
distance = []
for i in range(len(numbers)-1):
    distance.append(numbers[i+1] - numbers[i])
distance.sort()
if k >= len(distance):
    print(0)
else:
    answer = sum(distance[0:len(distance)-k+1])
    print(answer)
