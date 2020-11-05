"""This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom
lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def find_small(array):
    """
    Find the smallest item in array.

    Args:
        array: (array): write your description
    """
    mina = array[0][0]
    index = 0
    for ind in range(len(array)):
        if array[ind][0] < mina:
            index = ind
    return index


def big_all(value, array):
    """
    Return true if value is a list of integers.

    Args:
        value: (str): write your description
        array: (array): write your description
    """
    result = True
    for i in array:
        if i > value:
            result = False
    return result


intervals = [(30, 75), (0, 50), (60, 150)]

mins = []
for i in intervals:
    if len(mins) == 0:
        var = find_small(intervals)
        mins.append(intervals[var][1])
        del intervals[var]
    else:
        var = find_small(intervals)
        if not big_all(intervals[var][0], mins):
            mins.append(intervals[var][0])
        del intervals[var]

print(len(mins))
