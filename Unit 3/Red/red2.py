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
            result[i] = str(result[i]) + 'x'
        elif (len(funct) - 2 - i < 1):
            continue
        else:
            if (result[i] == 1):
                result[i] = 'x^' + str(len(funct) - 2 - i)
            else:
                result[i] = str(result[i]) + 'x^' + str(len(funct) - 2 - i)
    for elm in result:
        if elm == 0:
            result.remove(elm)
    if (str(result[-1]).isnumeric() and str(result[-2]).isnumeric()):
        if (-root < 0):
            result[-1] = str(result[-1]) + ' / (x - ' + str(root) + ')'
        else:
            result[-1] = str(result[-1]) + ' / (x + ' + str(root) + ')'
    return " + ".join(str(x) for x in result)

def evaluate (equation):
    temp = format(equation)
    print(temp)
    return synth_alg(temp[0], -int(temp[1][0]))

def format (string):
    result = [[], []]
    divisor = 0
    for index, elm in enumerate(string.split()):
        if (elm.strip() == '/'):
            divisor = 1
            continue
        if (elm.strip() == '+' or elm.strip() == '(' or elm.strip() == ')' or elm.strip() == ''):
            continue
        if (elm.replace('(', '')[0] == 'x' and divisor == 0):
            result[divisor].append(1)
        else:
            check = elm.split('x')[0].replace('(', '').strip()
            if (check == '' or check == '-'):
                continue
            result[divisor].append(int(elm.split('x')[0].replace('(', '').replace(')', '')))
            if (string.split()[index-1] == '-'):
                result[divisor][-1] = -int(result[divisor][-1])
    return result


'''
# Gap in terms and remainder in result
# (2x^4 + 6x^3 + 5x^2 - 44) / (x + 3) = 


2x^3 + 5x - 15 + 1 / (x + 3)

test = [2, 6, 5, 0 , -44] # 0 for missing linear term!!!
root = -3
print(synth_alg(test, root))
'''

print(evaluate('(2x^4 + 6x^3 + 5x^2 - 44) / (x + 3)'))