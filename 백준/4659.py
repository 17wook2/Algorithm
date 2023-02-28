def checkVowels(text):
    for e in text:
        if e in vowels:
            return True
    return False

def checkStrike(text):
    if len(text) < 3: return True
    for i in range(len(text)-2):
        new_text = text[i:i+3]
        cnt = 0
        for j in range(3):
            if new_text[j] in vowels: cnt += 1
        if cnt == 3 or cnt == 0:
            return False
    return True

def checkrow(text):
    if len(text) < 2: return True
    for i in range(len(text)-1):
        if text[i] == text[i+1] and text[i] != 'e' and text[i] != 'o':
            return False
    return True


while True:
    text = input()
    vowels = ['a','e','i','o','u']
    if text == "end":
        break
    if checkVowels(text) and checkStrike(text) and checkrow(text):
        print(f"<{text}> is acceptable.")
    else:
        print(f"<{text}> is not acceptable.")
