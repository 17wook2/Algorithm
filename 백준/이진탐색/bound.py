a = [1,2,3,3,3,4,5,6,7]
def upperbound(key):
    start = 0
    end = len(a)-1
    while start < end:
        mid = (start + end) // 2
        if a[mid] <= key:
            start = mid + 1
        else:
            end = mid - 1
    return start

def lowerbound(key):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = (start + end) // 2
        if a[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return start
def binarysearch(key):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1
print(upperbound(3))
print(lowerbound(3))
print(binarysearch(1))
print(binarysearch(8))