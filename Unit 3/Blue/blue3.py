alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encodeVigenere (code, cipher):
    global alph
    result = ''
    for x in range(len(code)):        
        result += alph[(alph.index(code[x]) + alph.index(cipher[x%len(cipher)]))%26]
    return result

def decodeVigenere (code, cipher):
    global alph
    result = ''
    for x in range(len(code)):        
        result += alph[(alph.index(code[x]) - alph.index(cipher[x%len(cipher)]))%26]
    return result

pt = "IFNJVRZLLDXZUESLXNUIKHH"
key = "GRADER"
dt = decodeVigenere(pt, key)
print(dt)