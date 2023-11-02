def swap(list_arg, index1, index2):
    temp = list_arg[index1]
    list_arg[index1] = list_arg[index2]
    list_arg[index2] = temp

def find_min_index(list_arg, start):
    # Finish this function so that it returns the index
    # of the minimum value in list_arg from the starting
    # index held in the argument 'start'
    min = 100000000000000
    for x in range(start, len(list_arg)):
        if (list_arg[x] < min):
            min = list_arg[x]
    return list_arg.index(min)

def selection_sort(list_arg):
    print("Selection sort")
    print("Start:", list_arg)
    for i in range(len(list_arg)-1):
        next_min = find_min_index(list_arg, i)
        swap(list_arg, i, next_min)
        print("Selection swap " + str(i) + ":", list_arg)


test_list = [15, 4, 11, 9, 7, 5, 10, 13, 17, 2]
selection_sort(test_list)