def sum_arithmetic(n_terms, start_val, inc_val):
    if (n_terms <= 1):
        return start_val
    return start_val + sum_arithmetic(n_terms-1, start_val+inc_val, inc_val)

def sum_geometric (n_terms, start_val, inc_val):
    if (n_terms <= 1):
        return start_val
    return start_val + sum_geometric(n_terms-1, start_val*inc_val, inc_val)


print(sum_arithmetic(11, 2, 3))
print(sum_geometric(5, 2, 0.8))