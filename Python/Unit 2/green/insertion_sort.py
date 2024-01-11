ls = [15, 4, 11, 9, 7, 5, 10, 13, 17, 2]

def insertion_sort (ls):      
    if len(ls) <= 1:
        return 
    for i in range(1, len(ls)):
        thisOne = ls[i]
        while i-1 >= 0 and thisOne < ls[i-1]:
            ls[i] = ls[i-1]
            x -= 1
        ls[i] = thisOne
  
insertion_sort(ls)