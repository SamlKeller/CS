'''
• encode_letter(letter, code_alpha) – this function takes two arguments. The argument letter will be
sent a string that is just a single capital letter. The argument code_alpha will be sent a string that contains a
scrambled alphabet – always 26 characters long, always capital letters. This function should return (not print)
the single letter that the given letter would be replaced with if using the given code alphabet to encode a
message.
o encode_letter("O", "TMGVBUZFNHWSPYKDXJOLERAICQ") should return "K", for example, as you
can see in the example cipher written above.
o This function should not contain any loops (for, while) or recursion. If you think one of those tools is
necessary, think a little more about the .index() command above!

• decode_letter(letter, code_alpha) – this works exactly like the previous function but in reverse,
receiving the encoded letter and returning the original.
o decode_letter("K", "TMGVBUZFNHWSPYKDXJOLERAICQ") should return "O", for example, to
match the previous example.

• substitution_encode(text, code_alpha) – this function takes two arguments. The argument text will
be sent a string of text that consists of only capital letters; code_alpha is a scrambled alphabet, as you’d
expect. This function should return (not print) that text encoded using the given code alphabet.
o substitution_encode("HELLO", "TMGVBUZFNHWSPYKDXJOLERAICQ") should return "FBSSK",
for example, to match the example at the top of the first page.
o You may find it helpful to have this function call encode_letter, though this is not required.
• substitution_decode(text, code_alpha) – text has been encoded using code_alpha to specify the
substitutions. Decode the same way. Return (do not print) the decoded string.
o substitution_decode("FBSSK", "TMGVBUZFNHWSPYKDXJOLERAICQ") should return "HELLO",
for example, to match the previous example.
o You may find it helpful to have this function call decode_letter, though this is not required.
'''

def encode_letter (letter, code_alpha):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if (letter.isalpha() == False):
        return letter
    if (letter.isupper() == False):
        return code_alpha.lower()[alphabet.lower().index(letter)]
    return code_alpha[alphabet.index(letter)]

def decode_letter (letter, code_alpha):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if (letter.isalpha() == False):
        return letter
    if (letter.isupper() == False):
        return  alphabet.lower()[code_alpha.lower().index(letter)]
    return alphabet[code_alpha.index(letter)]

def substitution_encode(text, code_alpha):
    string = ""
    for char in text:
        string += encode_letter(char, code_alpha)
    return string

def substitution_decode(text, code_alpha):
    string = ""
    for char in text:
        string += decode_letter(char, code_alpha)
    return string


'''
You should get this output EXACTLY.
'Dro qbokdocd psvwc yp kvv dswo gobo xofob wkno' - Dkivyb Cgspd, 2020
'The greatest films of all time were never made' - Taylor Swift, 2020
'''

def caesar_encode(txt, shift):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret = ''
    for char in txt:
        if (char.isalpha() == False):
            ret += char
            continue
        if (char.isupper() == False):
            if ((alph.lower().index(char)) + shift > 25):
                ret += alph.lower()[(alph.lower().index(char)+shift)-26]
            else:
                ret += alph.lower()[alph.lower().index(char)+shift]
        else:
            if ((alph.index(char) + shift) > 25):
                ret += alph[(alph.index(char)+shift)-26]
            else:
                ret += alph[alph.index(char)+shift]
    return ret

def caesar_decode(txt, shift):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret = ''
    for char in txt:
        if (char.isalpha() == False):
            ret += char
            continue
        if (char.isupper() == False):
            if (shift > alph.lower().index(char)):
                ret += alph.lower()[alph.lower().index(char)-shift]
            else:
                ret += alph.lower()[alph.lower().index(char)-shift]
        else:
            if (shift > alph.index(char)):
                ret += alph[(alph.index(char)-shift)]
            else:
                ret += alph[alph.index(char)-shift]
    return ret


pt = "SPHINX OF BLACK QUARTZ, HEAR MY VOW! sphinx of black quartz, hear my vow."
a2 = "GWCHBUFINAMKZTQELPSJYROVXD"
enc = substitution_encode(pt, a2)
dec = substitution_decode(enc, a2)
print(enc)
print(dec)

pt = "SPHINX OF BLACK QUARTZ, HEAR MY VOW! sphinx of black quartz, hear my vow."
shift = 8
enc = caesar_encode(pt, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)