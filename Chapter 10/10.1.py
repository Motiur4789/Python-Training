#10.1
from random import randrange

def random_list():
    '''
    Produce a list of pseudorandom integers.
    The list's length is chosen pseudorandomly in the
    range 3-20.
    '''
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result

def selection_sort(lst):
    '''
    Arranges the elements of list lst in ascending order.
    ©2011 Richard L. Halterman Draft date: November 13, 2011
    10.1. SORTING 209
    The contents of lst are physically rearranged.
    '''
    n = len(lst)
    for i in range(n - 1):
        # Note: i, small, and j represent positions within lst
        # lst[i], lst[small], and lst[j] represent the elements at
        # those positions.
        # small is the position of the smallest value we've seen
        # so far; we use it to find the smallest value less
        # than lst[i]
        small = i
        # See if a smaller value can be found later in the list
        # Consider all the elements at position j, where i < j < n
        for j in range(i + 1, n):
            if lst[j] < lst[small]:
                small = j 
        # Swap lst[i] and lst[small], if a smaller value was found
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]

def main():
    '''
    Tests the selection_sort function
    '''
    for n in range(3):
        col = random_list()
        print(col)
        selection_sort(col)
        print(col)
        print('==============================')
main()

