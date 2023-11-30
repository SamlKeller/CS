'''Convert this number: 212
From this base: 3
To this one: 16
Answer: 17'''

'''
Plan: 

When converting to and from bases on paper, I basically just use a mod operation to determine which numbers fall within which iteration of the base,
so I plan on creating an implementation that does the same.  Obviously at the end this needs to be integer divided to ensure that every number remains
within the base.  So, what I'll do is just convert to base ten first, then run the algorithm as I usually would and flip the string, which will then be
backwards.  Returning this should allow returning from and to any base.
'''

def baseConverter (num, base, orig):
    d = []
    num = convertToBaseTen(num, orig)
    if num < 1:
        return num
    while num:
        d.append(int(num % base))
        num //= base
    numsRange = d[::-1]
    final = ""
    for x in range(len(numsRange)):
        final += str(numsRange[x])
    return final

def convertToBaseTen (num, base):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    power = 0
    newNum = 0
    for digit in reversed(str(num)):
        newNum += chars.find(digit) * (base**power)
        power += 1
    return newNum

#The original string, the new base, and the original base
print(baseConverter("CE", 10, 16))