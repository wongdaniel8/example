import numpy as np


def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    processively swap elements in the list such that smaller ones come before larger ones, works on letters too
    """
    assignments, conditionals = 0, 0
    if len(x) == 0:
        conditionals += 1
        return  x, 0, 0
    new = x
    sort = False
    while(sort == False):
        conditionals += 1
        sort = True
        for i in range(0,len(x) - 1):
            conditionals += 1
            if new[i] > new[i+1]:
                sort = False
                first = new[i]
                second = new[i+1]
                new[i] = second
                new[i+1]= first
                assignments += 4
    return new, assignments, conditionals



rassignments, rconditionals = 0,0
def quicksort(a, p, r):
    global rassignments, rconditionals
    """
    Describe how you are sorting `x`
    divide and conquer approach to sort, find a pivot and place items smaller than pivot behind and items larger than pivot in front. Perform recursively.
    """
    if len(a) == 0:
        return a, 0, 0
    if len(a) == 1:
        return a, 0, 0 

    def partition(array, begin, end):
        global rassignments, rconditionals
        pivot = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                rconditionals += 1
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
                rassignments += 2
        array[pivot], array[begin] = array[begin], array[pivot]
        rassignments += 2
        return pivot

    if p >= r:
        return
    rconditionals += 1
    pivot  = partition(a, p, r)
    quicksort(a, p, pivot - 1)
    quicksort(a, pivot + 1, r)
    return a, rassignments, rconditionals



 ###partition function wrong
    # def partition(array, begin, end):
    #     pivot_item = a[begin]
    #     pivot = left = begin
    #     right = end
    #     while left < right: 
    #         while a[left] < pivot_item:
    #             left += 1
    #         while a[right] > pivot_item: 
    #             right -= 1 
    #         if left < right:
    #             tempL = left
    #             tempR = right 
    #             right = tempL
    #             left = tempR
    #     a[p] = a[right]
    #     a[right] = pivot_item
    #     return right

    # if p >= r:
    #     return
    # pivot = partition(a,p,r)
    # quicksort(a, p, pivot - 1)
    # quicksort(a, pivot + 1, r)
    # return a
    

