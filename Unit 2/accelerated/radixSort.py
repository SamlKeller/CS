'''
Another sorting algorithm that we haven’t learned is a Radix Sort. This assignment won’t tell you what it is, but there
are a lot of resources on the internet; in particular, the Wikipedia page for “Radix sort” might be all that you need. You
can search for anything you’d like in this assignment – this is a challenge not so much about figuring something out as
learning how something works. Any resources are fine here, but you only get credit if you can explain it on your own.
Your challenge:
 (2 points) Write a “Least significant digit” Radix Sort for positive integers (just like the example on Wikipedia).
Make your code so that it prints the list after each pass, so we can see each digit being taken into account one
by one. To get credit for this, you’ll need to:
o Show your code running (and demonstrating the sort) for several different test cases of different lengths
& numerical ranges
o Be able to explain how a Radix sort works on a whiteboard or a piece of paper, without referring to your
code or any notes
o Be able to explain how your code implements a Radix sort, line by line, and answer questions from your
teacher about it
'''


#This doesn't work with negatives -- should it?  I could make it work if I did another iteration with the 
#sign itself but I don't think this is a typical use case of radix so idk

def radixSort (ls):
    buckets = [[] for i in range(10)]
    maxDigits = 0
    for x in range(len(ls)): 
        if (ls[x] < 0): return "This function doesn't work with negative numbers"
        if (len(str(ls[x])) > maxDigits): maxDigits = len(str(ls[x]))
    for e in range(maxDigits):
        for i in range(len(ls)):
            if (len(str(ls[i])) > e):
                temp = str(ls[i])[-1-e]
            else:
                temp = str(ls[i])[0]
            buckets[int(temp)].append(ls[i])
        print(buckets)
        #flatten
        tempList = []
        for p in range(10):
            for r in range(len(buckets[p])):
                tempList.append(buckets[p][r])
        ls = tempList
        buckets = [[] for i in range(10)]
    return ls

print(radixSort([0, 1, 2, 22, 49, 550000, 1, 4, 2]))