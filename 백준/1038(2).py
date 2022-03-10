arr = []
def make(digit,number):
    if digit == 1:
        arr.append(number)
    for i in range(number%10):
        make(digit-1, number*10+i)
for i in range(10):
    for j in range(10):
        make(i+1,j)
n = int(input())
print(-1) if len(arr) <= n else print(arr[n])
