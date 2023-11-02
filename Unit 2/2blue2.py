from random import randint

def sum_all (name):
    with open('txt/' + name) as x:
        x = x.read()
        sum = 0
        xSplit = x.split()
        for i in range(0, len(xSplit)):
            sum += int(xSplit[i])
    return sum


def sum_all_first (name):
    with open('txt/' + name) as x:
        x = x.read().strip()
        sum = 0
        xSplit = x.split('\n')
        for i in range(0, len(xSplit)):
            sum += int(xSplit[i].split()[0])
    return sum

def sum_all_special (name):
    with open('txt/' + name) as x:
        x = x.read()
        sum = 0
        xSplit = x.split()
        for i in range(0, len(xSplit)):
            if (int(xSplit[i]) % 10 < int(xSplit[i]) % 100 // 10):
                sum += int(xSplit[i])
    return sum


def sum_all_commas (name):
    with open('txt/' + name) as x:
        x = x.read()
        sum = 0
        x = x.replace('\n', ',')
        xSplit = ''.join(x.split())
        xSplit = xSplit.split(',')
        for i in range(0, len(xSplit)-1):
            sum += int(xSplit[i])
    return sum


def createProblemOne (name):
    file = open('txt/' + name,"w+")
    string = ''
    for lines in range(0, randint(10, 20)):
        for ints in range(0, randint(3, 15)):
            string += str(randint(1, 99)) + " "
        string += '\n'
    file.write(string)