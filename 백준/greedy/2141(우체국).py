n = int(input())
info = []
for i in range(n):
    info.append(list(map(int,input().split())))

info.sort(key = lambda x:x[0])
population = []
for i in info:
    population.append(i[1])
# print(population)

start = 0
end = n-1
temp = int(1e9)
while start <= end:
    mid = (start+end) // 2
    left = sum(population[:mid+1])
    right = sum(population[mid+1:])
    if left >= right:
        end = mid - 1
        temp = min(temp, info[mid][0])
    else:
        start = mid + 1
print(temp)