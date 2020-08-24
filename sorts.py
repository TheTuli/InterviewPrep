__author__ = "rt3991@rit.edu"

"""
    Merge Sort(Not in place)
    
    (1) Brute Force Approach
            Time Complexity     : O( nlog(n) )
            Space Complexity    : O( nlog(n) )
        
            GIST    : 
                    
                    > Divide the array till you have one element
                    > Array of 1 element is sorted
                    > Merge Two Sorted arrays into a third sorted array
                    > Return new sorted array
"""


def merge_sort(arr):
    """
    >>> merge_sort([3, 2, 1])
    [1, 2, 3]

    >>> merge_sort([6, 4, 3, 1, 2, 9])
    [1, 2, 3, 4, 6, 9]
    """
    if len(arr) < 2:
        return arr

    left, right = divide(arr)
    left = merge_sort(left)
    right = merge_sort(right)
    return _merge(left, right)


def divide(arr):
    return arr[:len(arr) // 2], arr[len(arr) // 2:]


def _merge(arr1, arr2):
    """
    A linear time algorithm to merge two sorted lists

    Complexity: Time Complexity Linear "Big-oh" O(m + n)
                Where,
                m = length of first list, and
                n = length of second list

                Space Complexity Linear same as above,
                because we create a new third array of length: m + n

    :post-condition: destroys the two input arrays
    """
    new_array = []

    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            new_array.append(arr1.pop(0))
        else:
            new_array.append(arr2.pop(0))

    # if more elements in either array
    new_array.extend(arr1)
    new_array.extend(arr2)

    return new_array


if __name__ == '__main__':
    import doctest

    doctest.testmod()
