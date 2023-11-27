def largest_value(num_list):
    largest = 0
    for x in num_list:
        if (x > largest):
            largest = x
    return largest

def largest_index(num_list):
    largest = 0
    index = 0
    for x in range(0, len(num_list)):
        if (num_list[x] > largest):
            largest = num_list[x]
            index = x
    return index

def second_largest_value(num_list):
    largest = 0
    secondLargest = 0
    for x in num_list:
        if (x > largest):
            largest = x
    for x in range(1, len(num_list)):
        if (num_list[-x] < largest and num_list[-x] > secondLargest):
            secondLargest = num_list[-x]
    return secondLargest



print(largest_value([2, 7, 2, 78, 2, 6, 2]))