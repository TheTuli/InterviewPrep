"""
    Median of two sorted arrays
    example:

    >>> arr1 = [1, 2, 3]
    >>> arr2 = [4, 5, 6]
    >>> get_median(arr1, arr2)
    3.5

"""


def get_median(arr1, arr2):
    """
    Driver function to run different algorithms
    """
    return median_brute_force(arr1, arr2)


def median_brute_force(arr1, arr2):
    """
    Algorithm:

    Merge both arrays in linear time;

    :return the middle element if merged array is of odd length,
    else return the mean of the middle two elements

    Complexity: Time Complexity Linear "Big-oh" O(m + n)
                due to the merge operation,
                Where,
                m = length of first list, and
                n = length of second list

                Space Complexity Linear same as above,
                because we create a new third array of length: m + n
    Tests:
    >>> median_brute_force([1, 2, 3], [4, 5, 6])
    3.5

    >>> median_brute_force([],[])
    Traceback (most recent call last):
    ...
    IndexError

    >>> median_brute_force([1, 2, 3], [4, 5])
    3

    >>> median_brute_force([1, 2], [3, 4, 5, 6])
    3.5
    """

    def _merge():
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

    merged_array = _merge()
    return _get_middle_value(merged_array)


def _get_middle_value(a_list):
    """
    Gets the middle data of a list

    Complexity: Constant time operation hence "Big-oh" O(1)

    :pre-condition: The list should not be empty

    >>> _get_middle_value([1, 2, 3])
    2

    >>> _get_middle_value([1, 2, 3, 4])
    2.5

    >>> _get_middle_value([])
    Traceback (most recent call last):
    ...
    IndexError

    """
    if not a_list:
        raise IndexError

    if len(a_list) & 1 == 1:
        return a_list[len(a_list) // 2]

    return (a_list[len(a_list) // 2 - 1] + a_list[len(a_list) // 2]) / 2.0


def median_brute_force_optimized(arr1, arr2):
    """
    Same Algorithm as above, but without creating a new array
    Complexity: Time Complexity Linear "Big-oh" O(m + n)
                Where,
                m = length of first list, and
                n = length of second list

                Space Complexity Constant "Big-oh" O(1)
                because we do not create a new array.
    Tests:
    >>> median_brute_force_optimized([1, 2, 3], [4, 5, 6])
    3.5

    >>> median_brute_force_optimized([],[])
    Traceback (most recent call last):
    ...
    IndexError

    >>> median_brute_force_optimized([1, 2, 3], [4, 5])
    3

    >>> median_brute_force_optimized([1, 2], [3, 4, 5, 6])
    3.5
    """

    new_array_length = len(arr1) + len(arr2)

    if new_array_length & 1 == 1:
        return _get_element_without_merging(arr1, arr2, new_array_length // 2)

    return (
                   _get_element_without_merging(arr1, arr2,
                                                new_array_length // 2 - 1) +
                   _get_element_without_merging(arr1, arr2,
                                                new_array_length // 2)
           ) / 2.


def _get_element_without_merging(arr1, arr2, index):
    """
    >>> _get_element_without_merging([4, 5, 6], [1, 2, 3], 2)
    3

    >>> _get_element_without_merging([], [], 0)
    Traceback (most recent call last):
    ...
    IndexError

    >>> _get_element_without_merging([], [1, 2, 3], 0)
    1

    >>> _get_element_without_merging([1], [2, 3], 0)
    1

    >>> _get_element_without_merging([1], [2, 3], 1)
    2

    >>> _get_element_without_merging([1, 2], [2, 3], 1)
    2

    """
    k, i, j = 0, 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            current_element = arr1[i]
            i += 1

        else:
            current_element = arr2[j]
            j += 1

        if k == index:
            return current_element

        k += 1

    if i < len(arr1) and (index - k) < (len(arr1) - i):
        return arr1[i + (index - k)]

    if j < len(arr2) and (index - k) < (len(arr2) - j):
        return arr2[j + (index - k)]

    raise IndexError


def max_left(arr, partition):
    """
    Considers elements before partition
    """
    if partition == 0:
        return -float('inf')

    return arr[partition - 1]


def min_right(arr, partition):
    """
    Considers elements on and after partition
    """
    if partition == len(arr):
        return float('inf')

    return arr[partition]


def median_logarithmic(arr1, arr2):
    """
    >>> median_logarithmic([1, 2, 3], [4, 5, 6])
    3.5
    >>> median_logarithmic([1, 2, 3], [4, 5, 6])
    3.5

    >>> median_logarithmic([1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 10, 10, 10])
    3.5

    >>> median_logarithmic([], [1, 2, 3])
    2
    """
    if len(arr1) == 0:
        return _get_middle_value(arr2)
    elif len(arr2) == 0:
        return _get_middle_value(arr1)

    if len(arr1) > len(arr2):
        return median_logarithmic(arr2, arr1)

    len_first, len_second = len(arr1), len(arr2)

    low, high = 0, len_first
    i = 0
    while low <= high:

        i += 1
        partition_first = (low + high) // 2
        partition_second = (len_first + len_second + 1) // 2 - partition_first


        max_left_first, max_left_second = max_left(arr1, partition_first), \
                                          max_left(arr2, partition_second)
        min_right_first, min_right_second = min_right(arr1, partition_first), \
                                            min_right(arr2, partition_second)

        if max_left_first <= min_right_second and max_left_second <= min_right_first:
            if (len_first + len_second) & 1 == 1:
                return max(max_left_first, max_left_second)

            return (
                           max(max_left_first, max_left_second) +
                           min(min_right_first, min_right_second)
                   ) / 2

        if max_left_first > min_right_second:
            # Move left in first array
            high = partition_first - 1

        else:

            low = partition_first + 1

        if i == 10:
            break
    return "NOT FOUND"


if __name__ == '__main__':
    import doctest

    doctest.testmod()
