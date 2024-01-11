def tNums(num):
    nums = []
    for n in range(num):
        nums.append(int( (n*(n+1)) / 2 ))
    return nums

def synth_alg (funct, root):
    result = [funct[0]]
    for x in range(1, len(funct)):
        result.append((result[-1]*root) + funct[x])
    for i in range(len(result)-1):
        if (result[i] == 0):
            continue
        elif (len(funct) - 2 - i == 1):
            if (result[i] == 1):
                result[i] = 'x'
            #result[i] = str(result[i]) + 'x'
        elif (len(funct) - 2 - i < 1):
            continue
        else:
            if (result[i] != 'x'): 
                if (result[i] == 1):
                    result[i] = 'x^' + str(len(funct) - 2 - i)
                elif (result[i] == -1):
                    result[i] = '-x^' + str(len(funct) - 2 - i)
                else:
                    result[i] = str(result[i]) + 'x^' + str(len(funct) - 2 - i)
    for elm in result:
        if elm == 0:
            result.remove(elm)
    if ('x' not in str(result[-2])):
        result.append('/ (x - ' + str(root) + ')')
    temp = " + ".join(str(x) for x in result)
    if ('+ / ' in temp):
        return temp.split(' + / ')[0] + ' / ' +  temp.split(' + / ')[1]
    return temp

def evaluate (equation):
    temp = format(equation)
    return synth_alg(temp[0], -int(temp[1][0]))

def getExponent (elm, lastExponent):
    elm = elm.strip()
    if (elm == '-' or elm == '+'):
        return int(lastExponent) - 1
    if ('x' not in elm):
        return 1
    elif ('^' not in elm):
        return 1
    else:
        return int(elm.split('x^')[1])

def format (string):
    result = [[], []]
    divisor = 0
    firstExponent = int(string.split()[0].split('^')[1])
    lastExponent = firstExponent
    for index, elm in enumerate(string.split()):
        if (elm.strip() == '/'):
            divisor = 1
            continue
        if (elm.strip() == '+' or elm.strip() == '(' or elm.strip() == ')' or elm.strip() == ''):
            continue
        if ((getExponent(elm, lastExponent) != int(lastExponent) - 1) and (getExponent(elm, lastExponent) != lastExponent or lastExponent == 2 and 'x' not in elm.strip()) or (getExponent(elm, lastExponent) == 1 and 'x^2' in string.split()[index-2] and 'x' not in elm)):
            result[0].insert(index-1, 0)
        if (elm.replace('(', '')[0] == 'x' and divisor == 0):
            if (string.split()[index-1].strip() == '-'):
                result[divisor].append(-1)
            else:
                result[divisor].append(1)
        else:
            if (lastExponent != 1):
                lastExponent = getExponent(elm, lastExponent)
            check = elm.split('x')[0].replace('(', '').strip()
            if (check == ''):
                continue
            if (string.split()[index-1].strip() == '-'):
                if (elm.split('x')[0].replace('(', '').replace(')', '') != '-'):
                    result[divisor].append(-1*int(elm.split('x')[0].replace('(', '').replace(')', '')))
            else:
                if (elm.split('x')[0].replace('(', '').replace(')', '') != '-'):
                    result[divisor].append(int(elm.split('x')[0].replace('(', '').replace(')', '')))
    return result

[[2, 5, -1, 6, 1, 2], [-3]]

''''
# Standard example
# (2x^2 + 11x + 15) / (x + 3) = 2x + 5
test = [2, 11, 15]
root = -3
print(synth_alg(test, root))
>> "2x + 5"

# Higher Power
# (x^4 - 3x^3 + 5x^2 - 17x + 6) / (x - 3) = x^3 + 5x - 2
test = [1, -3, 5, -17, 6]
root = 3
print(synth_alg(test, root))
>> "x^3 + 5x + -2"

# Remainder in result
# (x^4 - 5x^3 + 7x^2 - 34x - 1) / (x - 5) = x^3 + 7x + 1 + 4 / (x - 5)
test = [1, -5, 7, -34, -1]
root = 5
print(synth_alg(test, root))
>> "x^3 + 7x + 1 + 4 / (x - 5)"

# Gap in terms and remainder in result
# (2x^4 + 6x^3 + 5x^2 - 44) / (x + 3) = 2x^3 + 5x – 15 + 1 / (x + 3)
test = [2, 6, 5, 0 , -44] # 0 for missing linear term!!!
root = -3
print(synth_alg(test, root))
>> "2x^3 + 5x + -15 + 1 / (x - -3)"
'''
print(evaluate('(5x^4 - 10x^3 + x^2 - 6x + 8 / (x - 2)')) #5x^3 + x - 4
print(evaluate('(2x^5 + 5x^4 - x^3 + 6x^2 + x + 2 / (x + 3)')) #2x^4 − x^3 + 2x^2 + 1 + −1 / x+3
print(evaluate('(2x^4 + 6x^3 + 5x^2 - 44) / (x + 3)')) # 2x^3 + 5x – 15 + 1 / (x + 3)