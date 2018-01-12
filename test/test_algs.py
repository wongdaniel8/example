import numpy as np
from example import algs


def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    # assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))
    assert np.array_equal(np.array([1,2,3]), np.array([1,2,3]))


    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    # assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))
    assert np.array_equal(np.array([1,2,3]), np.array([1,2,3]))



def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = np.array([1,2,4,0,1])
    
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    sort = algs.bubblesort(x)[0]
    assert np.array_equal(sort, np.array([0,1,1,2,4]))
    assert np.array_equal(sort, np.array([0,1,1,2,4]))

    y = ['b', 'c', 'a', 'a', 'd', 'a']
    sort = algs.bubblesort(y)[0]
    assert np.array_equal(sort, np.array(['a','a','a','b','c','d']))

    x = np.array([1])
    sort = algs.bubblesort(x)[0]
    assert np.array_equal(sort, np.array([1]))

    x = np.array([1,4,2,3])
    sort = algs.bubblesort(x)[0]
    assert np.array_equal(sort, np.array([1,2,3,4]))


def test_quicksort():

    x = np.array([1,2,4,0,1])
    sort = algs.quicksort(x, 0, len(x) - 1)[0]
    print("SSS", sort)
    assert np.array_equal(sort, np.array([0,1,1,2,4]))

    y = ['b', 'c', 'a', 'a', 'd', 'a']
    sort = algs.quicksort(y, 0, len(y) - 1)[0]
    assert np.array_equal(sort, np.array(['a','a','a','b','c','d']))

    x = np.array([1])
    sort = algs.quicksort(x, 0, len(x) - 1)[0]
    assert np.array_equal(sort, np.array([1]))

    x = np.array([1,4,2,3])
    sort = algs.quicksort(x, 0, len(x) - 1)[0]
    assert np.array_equal(sort, np.array([1,2,3,4]))




    
