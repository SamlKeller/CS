def replace_after (string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y'] # Should y always be a vowel?
    string = list(string)
    lastChar = ''
    for index, char in enumerate(string):
        if (lastChar.upper() in vowels):
            string[index] = '!'
        lastChar = char
    return "".join(str(x) for x in string)

def before_after (string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    result = ''
    for x in range(len(string)):
        if (string[x].upper() in vowels):
            if (result[-1] == '!'):
                result += string[x] + '!'
            else:
                result += '!' + string[x] + '!'
        else: 
            result += string[x]
    return result

def pairs (string):
    arr = []
    for index, char in enumerate(string):
        if (index - 1 < 0):
            continue
        arr.append(string[index-1] + char)
    return arr

def either35 (ls):
    lastElm = ''
    threeFive = False
    fiveThree = False
    for elm in ls:
        if (elm == 5):
            if (lastElm == 5):
                threeFive = True
        elif (elm == 3):
            if (lastElm == 3):
                fiveThree = True
        lastElm = elm
    return (fiveThree or threeFive) and ((fiveThree == False) or (threeFive == False))

def five_run (ls):
    brokeFive = False
    lastFive = 0
    for index, elm in enumerate(ls):
        if (brokeFive == False):
            if (elm >= 5):
                brokeFive = True
            else:
                continue
        if (elm % 5 == 0):
            lastFive = elm
        else:
            ls[index] = lastFive
    return ls

def every_third (string):
    string = list(string)
    string[0] = '!'
    for x in range(len(string)):
        if (x % 3 == 0):
            string[x] = '!'
    return "".join(str(x) for x in string)