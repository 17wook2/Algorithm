s = input()
res = 0
def func(string):
    length = len(string)
    table = [0]*length
    j = 0
    for i in range(1,length):
        while j > 0 and string[i] != string[j]:
            j = table[j-1]
        if string[i] == string[j]:
            j += 1
            table[i] = j
    return max(table)

for i in range(len(s)):
    sub_str = s[i:len(s)]
    res = max(res,func(sub_str))

print(res)