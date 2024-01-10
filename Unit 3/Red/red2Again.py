''''
>> "2x^3 + 5x + -15 + 1 / (x - -3)"
#print(evaluate('(5x^4 - 10x^3 + x^2 - 6x + 8 / (x - 2)')) #5x^3 + x - 4
print(evaluate('(2x^5 + 5x^4 - x^3 + 6x^2 + x + 2 / (x + 3)'))
'''


# (2x^4 + 6x^3 + 5x^2 - 44) / (x + 3) => [2, 6, 5, 0 , -44] [-3]

def format (string):
    result = [[], []]
    print(string.split())
    nextElm = 1
    divider = 0
    exponents = []
    for index, elm in enumerate(string.split()):
        if (elm == '-'):
            nextElm = -1
        elif (elm == '/'):
            divider = 1
        elif (elm == '+'):
            continue
        elif ('x^' in elm):
            result[divider].append(elm.split('x^')[0])
        elif ('x' in elm):
            result[divider].append(elm.split('x')[0])
            




format('(2x^4 + 6x^3 + 5x^2 - 44) / (x + 3)')