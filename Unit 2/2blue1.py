'''
1) Write a while loop that makes a list of every positive number that is a multiple of 3 or 5 less than 1000. The list
should not include the number 0 or the number 1000.

2) Modify the above code to create a function list_mults that accepts two arguments and returns a list of every
number that is a multiple of 3 or 5 between the two values it receives.
    o For example, list_mults(100, 111) would return [102, 105, 108, 110]

3) Write a function all_odds that takes a single number and returns True if every single digit of the given
number is an odd digit. False if any digit is even.
    o For example, all_odds(153719) would return True
    o For example, all_odds(1345) would return False, because of the 4

4) Write a function make_fibos that takes a single integer argument and uses a while loop to return a list of all
the Fibonacci numbers less than that value. (You can assume the value will never be less than 2.)
    o For example, make_fibos(100) would return [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    o Hint: remember that, no matter how long a list is, list[-1] will always access the last element in it,
      and list[-2] will always access the second to last element in it, etc.
'''

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