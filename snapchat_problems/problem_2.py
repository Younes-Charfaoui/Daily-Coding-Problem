"""This problem was asked by Snapchat.
Given a list of possibly overlapping intervals, return a new list of 
intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)]
"""


def find_small(array):
    mina = array[0][0]
    index = 0
    for ind in range(len(array)):
        if array[ind][0] < mina:
            index = ind
    return index


intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]

result = []

for i in range(len(intervals)):
    var = find_small(intervals)
    result.append(intervals[var])
    del intervals[var]

print(result)
