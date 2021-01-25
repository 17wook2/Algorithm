from itertools import permutations
import math
def solution(numbers):
    prime = []
    for i in range(1,len(numbers)+1):
        lst = makePermutation(numbers,i)
        for item in lst:
            if checkPrime(item) and item not in prime:
                prime.append(item)
    return len(prime)

def checkPrime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2,int(math.sqrt(number))+1,1):
        if number % i == 0:
            return False
    return True
def makePermutation(number,idx):
    return list(map(int,list(map(''.join, list(permutations(list(number),idx))))))
a = [1,2,3]
print(a[0:0])