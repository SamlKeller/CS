import time
import math

'''
Determining whether or not a number is prime is a great algorithm to figure out on your own! If you’ve forgotten what
a prime number is, feel free to ask your teacher.
You should also know that “twin prime” numbers are prime numbers that are only a distance of 2 apart. For example,
17 and 19 are a pair of twin prime numbers, as are 71 and 73, but 19 and 23 are too far apart.
To do any part of this problem, you will need to write an honor code statement at the top of your code which reads:
I swear, on my honor, I did not google any solutions, algorithms, or Python code related to this
problem, or get another person to give me any solutions, algorithms or Python code related to this
problem. I solved it entirely myself. -Your name
Your challenges:
 Figure out a way to write a function that takes a number and returns True if that number is prime, and False if
that number isn’t prime. Then, use your is_prime function and write a new function that will take a number, n,
and find the number of pairs of twin primes less than n. For instance, there are 4 pairs of twin primes less than
20: 3 and 5, 5 and 7, 11 and 13, 17 and 19.
 (1 point) If your code can generate the number of pairs of twin primes less than 10,000 in less than 10 seconds,
you get one point. (You may not store this information in a .txt file or hardcoded within your .py file; your code
has to generate it from scratch.)
 (1 point) If your code can generate the number of pairs of twin primes less than 1,000,000 in less than 10
seconds, you get an additional point for a total of 2. (You may not store this information in a .txt file or
hardcoded within your .py file; your code has to generate it from scratch.)
'''


'''
I swear, on my honor, I did not google any solutions, algorithms, or Python code related to this
problem, or get another person to give me any solutions, algorithms or Python code related to this
problem. I solved it entirely myself. -Samuel Stankiewicz
'''


def isPrime (num):
    #technically this function is not completely correct; it will return true for 1, but given the use case it doesn't matter
    for x in range(3, int(math.sqrt(num)+1), 2):
        if (num % x == 0):
            return False
    return True

def getTwinPrimesLessThanNum (num):
    lastPrime = 2
    primesCounter = 0
    if (num == 6):
        return 1
    for x in range(1, num, 2):
        if (isPrime(x)):
            if (lastPrime == x - 2):
                primesCounter += 1
            lastPrime = x
    return primesCounter-1

start_time = time.time()
print("Number of twin primes:", getTwinPrimesLessThanNum(10000))
print("Completed in", (time.time() - start_time), "seconds")