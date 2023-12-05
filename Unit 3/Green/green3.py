
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



# I feel like the technical viability of this function is extremely low but maybe i'm wrong

def caesar_crack(txt):
    highestETA = 0
    theCrack = ''
    for x in range(1, 26):
        temp = caesar_decode(txt, x)
        tempCount = caesar_decode(txt, x).count('a') + caesar_decode(txt, x).count('A') + caesar_decode(txt, x).count('t') + caesar_decode(txt, x).count('T') + caesar_decode(txt, x).count('e') + caesar_decode(txt, x).count('E')
        if (tempCount > highestETA):
            highestETA = tempCount
            theCrack = temp
    return theCrack


print(caesar_crack('Dszce lyo dhppe'))

pt = "SPHINX OF BLACK QUARTZ, HEAR MY VOW! sphinx of black quartz, hear my vow."
shift = 8
enc = caesar_encode(pt, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)


'''
1. 'M wex hsar erh avsxi xli jmvwx gsqtmpiv. Mx aew zivc wxytmh. Alex M hmh aew
aexgl qcwipj tyx xskixliv e tvskveq erh qeoi xli gsqtyxiv hs alex M hmh.' - Kvegi
Lsttiv, gsqtyxiv wgmirxmwx erh qmpmxevc ehqmvep


->> 'I sat down and wrote the first compiler. It was very stupid. What I did was
watch myself put together a program and make the computer do what I did.' - Grace
Hopper, computer scientist and military admiral


2. 'Pgpcjmzoj dszfwo wplcy ez aczrclx l nzxafepc, mpnlfdp te eplnspd jzf szh ez
estyv.' - Depgp Uzmd, qzcxpc NPZ lyo ncplezc zq Laawp


->> 'Everybody should learn to program a computer, because it teaches you how to
think.' - Steve Jobs, former CEO and creator of Apple

3. 'Max Bgmxkgxm? Px tkx ghm bgmxkxlmxw bg bm.' - Ubee Ztmxl, yhngwxk hy Fbvkhlhym, 1993


->> 'The Internet? We are not interested in it.' - Bill Gates, founder of Microsoft, 1993

lol that aged well

'''