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
    fives = False
    for x in range(len(ls)):
        if (ls[x] % 5 == 0):
            fives = True
    if (fives == False):
        return ls
    print(fives)
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


print(replace_after("loosely"))
print(before_after("freeloopers"))
print(pairs("LONGER"))
print(either35([3, 3, 5, 3, 5, 5]))
print(either35([3, 5, 3, 5, 5]))
print(either35([3, 3, 5, 3, 5]))
print(either35([3, 5, 3, 5]))
print(five_run([20, 1, 15, 7, 8, 5, 0, 8]))
print(five_run([21, 1, 14, 7, 8, 4, 1, 8]))
print(every_third("ooooh nooooo"))

'''1) Write a function replace_after that replaces every letter after a vowel with a “!”.
o For example, replace_after("steerage") should return "ste!!a!e" - CAREFUL WITH THIS ONE it
should not return "ste!ra!e", which is a common mistake!

2) Write a function before_after that adds exclamation points before and after each vowel, but without
replacing any characters. But: you shouldn’t ever have two exclamation points in a row.
o For example, before_after("steerage") should return "st!e!e!r!a!g!e!" – note there’s only
one exclamation mark between the two "e"s.

3) Write a function pairs that returns a list of every 2-character substring of the original string.
o For example: pairs("CATS") would return ["CA", "AT", "TS"]
4) Write a function either35 that accepts a list of ints and returns True if the list contains a 3 next to a 3 or a 5
next to a 5, but not both. Examples:
o either35([1, 3, 3]) → True
o either35([5, 5, 1]) → True
o either35([5, 5, 1, 3, 3]) → False
5) Write a function five_run that takes a list and changes each value following a multiple of 5 to the current
multiple of 5 until encountering another multiple of 5. Examples:
o five_run([1, 2, 5, 6, 4, 5, 9, 10, 11, 13, 15]) → [1, 2, 5, 5, 5, 5, 5, 10,
10, 10, 15]
o five_run([30, 1, 9, 15]) → [30, 30, 30, 15]
6) Write a function every_third that returns a string made by replacing every third character of the original
string with an exclamation point, starting at index 0. Examples:
o "ExampleString" → "!xa!pl!St!in!"
o "eeeeeeeee" → "!ee!ee!ee" (careful with this one!)'''

print(every_third("eeeeeeeee"))