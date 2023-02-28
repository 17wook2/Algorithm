text = input()
def isJava(text):
    if not text[0].isalpha() or text[0].isupper(): return False
    for i in range(1,len(text)):
        if not text[i].isalpha(): return False
    return True

def isCpp(text):
    if text[0] == '_' or text[-1] == '_': return False
    for i in range(len(text)):
        if text[i] != '_' and text[i].isupper(): return False
    return True

if isJava(text) and isCpp(text):
    print(text)
elif isJava(text) or isCpp(text):
    ans = ''
    if isJava(text):
        for i in range(len(text)):
            if text[i].isupper():
                ans += '_'
                ans += text[i].lower()
            else:
                ans += text[i]
    else:
        splited = text.split("_")
        ans += splited[0]
        if len(splited) > 1:
            for i in range(1,len(splited)):
                ans += splited[i].title()
        print(ans)
else:
    print("Error!")


