def demoC():
    s = "string"
    x = len(s)
    print(x)
    r = "longerstring"
    y = len(r)
    print(y)

def demoD():
    s = "string"
    new_string = s[1:3]
    print(new_string)

def slice_end(str, index):
    return str[index:]

def pig_latin (str):
    return str[1:] + str[0] + 'ay'

def shrink (str):
    if (len(str) == 0):
        return
    print(str)
    shrink(str[0:len(str)-1])

def grow (str):
    if (len(str) == 0):
        return
    grow(str[0:len(str)-1])
    print(str)

first = 0
def shrink_right(str):
    global first
    if (len(str) > first):
        first = len(str)
    if (len(str) == 0):
        return
    print(" " * (first - len(str)) + " " + str)
    shrink_right(str[1:])


startingStr = 0
def word_cascade (str):
    global startingStr
    if (len(str) > startingStr):
        startingStr = len(str)
    if (len(str) == 0):
        return
    word_cascade(str[0:len(str)-1])
    print((len(str)-1) * " " + str)
    if (len(str) == startingStr):
        iterate_backwards(str, str[1:len(str)])
        
def iterate_backwards (original, str):
    if (len(str) == 0):
        return
    print((((len(original)-len(str))+len(original)) * " ") + str)
    iterate_backwards(original, str[1:len(str)])


startingStrBackwards = 0
def cascade_backwards (str):
    grow_right(str, str)
    shrink(str[0:len(str)-1])


firstGrow = 0
def grow_right(original, str):
    global firstGrow
    if (len(str) == 0):
        return
    if (len(str) > firstGrow):
        firstGrow = len(str)
    grow_right(original, str[1:])
    print((len(original) - len(str))*" " + str)


def shrink (str):
    if (len(str) == 0):
        return
    print(str)
    shrink(str[0:len(str)-1])


def snake (str):
    if (len(str) < 1):
        return
    print(len(str)*" " + str[1])
    return snake(str[1::])

#snake("snakesinthegrass")

'''
Between 4 and 8, 12 and 16, etc

counter % 2 > 0

0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0

c
 o
--u
 n
t
 e
  r

'''

'''
snake("snakesinthegrass")
s
 n
  a
 k
e
 s
  i
 n
t
 h
  e
 g
r
 a
  s
 s
'''

def generateSequence (n):
    if (n == 0):
        return ""
    spaces = n%3
    print((spaces*" ") + generateSequence(n-1) + "x")
    return ""

print(generateSequence(20))