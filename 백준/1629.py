[A,B,C] = list(map(int,input().split()))
# print(A,B,C)
def power(A,B,C):
    if B == 1:
        return A % C
    else:
        temp = power(A,B//2,C)
    if B %2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp) * power(A,1,C) % C
print(power(A,B,C))
