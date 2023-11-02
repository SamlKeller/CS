def mult35less1000 ():
    list = []
    iterator = 1000
    while (iterator > 3):
        iterator -= 1
        if (iterator % 5 == 0 or iterator % 3 == 0):
            list.append(iterator)
    return list

def list_mults (a, b):
    list = []
    iterator = b
    while (iterator > a+1):
        iterator -= 1
        if (iterator % 5 == 0 or iterator % 3 == 0):
            list.append(iterator)
    return list[::-1]

def all_odds (num):
    for x in range(0, len(str(num))):
        if (int(str(num)[x]) % 2 != 0):
            continue
        else:
            return False
    return True

def make_fibos(num):
    n = 0
    fibs = []
    while (generate_fib(n) < num):
        fibs.append(generate_fib(n))
        n += 1
    return fibs

def generate_fib (num):
    fibs = [0, 1]
    for i in range(2, num+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[num]