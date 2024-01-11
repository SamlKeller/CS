def sum_n (n):
    if (n == 0):
        return n
    return n + sum_n(n-1)

def sum_squares (n):
    if (n == 0):
        return 0
    return n**2 + sum_squares(n-1)

def sum_even(n):
    if n == 0:
        return n
    elif n % 2 == 0:
        return n + sum_even(n-2)
    elif n % 2 == 1:
        return n + sum_even(n-1)
    
def count_threes(n):
    if (n <= 0):
        return n
    return 1 + count_threes(n-3)

def sum_m_to_n (m, n):
    if (m <= n):
        if (m > n):
            return n + sum_m_to_n(m, n+1)
        return n + sum_m_to_n(m, n-1)
    return 0

def product_m_to_n (m, n):
    print(m, n)
    if (m < n):
        if (m > n):
            return n * product_m_to_n(m, n+1)
        return n * product_m_to_n(m, n-1)
    return n

def sum_no_3_5(n):
    print(n)
    if (n <= 0):
        return n
    if (n % 5 != 0 and n % 3 != 0):
        print(n)
        return n + sum_no_3_5(n-1)
    return sum_no_3_5(n-1)

def ends_with_1_or_3_original (n):
    print(n)
    if (n % 10 == 1 or n % 10 == 3):
        print(n, "ends with 1 or 3")
        return True
    return False
    
def sum_ends_1_or_3_original (n):
    if (n <= 0):
        return n
    if (ends_with_1_or_3(n)):
        return n + sum_ends_1_or_3(n-1)
    return sum_ends_1_or_3(n-1)

def ends_with_1_or_3 (n):
    if (n % 10 == 1 or n % 10 == 3):
        print(n, 'ends with 1 or 3')
        return True
    return False

def sum_ends_1_or_3 (n):
    if n == 0:
        return 0
    elif ends_with_1_or_3(n):
        temp = sum_ends_1_or_3(n - 1)
        print(n)
        return n + temp
    elif not ends_with_1_or_3(n):
        print(n)
        return sum_ends_1_or_3(n - 1)
    
def print_bouncy_sum (s, f):
    if (s == f):
        return s
    if (len(str(s)) != 3):
        # not bouncy
        return print_bouncy_sum(s+1, f)
    if (int(str(s)[0]) < int(str(s)[1]) and int(str(s)[2]) < int(str(s)[1])):
        # bouncy
        print(s, "is bouncy")
        return s + print_bouncy_sum(s+1, f)
    return print_bouncy_sum(s+1, f)

def print_sum_ends_1_or_3_results (n):
    print("The final sum is", sum_ends_1_or_3(n))



print(print_bouncy_sum(400, 600))