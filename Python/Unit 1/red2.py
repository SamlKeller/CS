def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm (a, b):
    return (a*b)//gcd(a, b)

def lcm_n (n):
    if (n == 1):
        return n
    return lcm(lcm_n(n-1), n)

print(lcm_n(100))