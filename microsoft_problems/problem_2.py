"""This problem was asked by Microsoft.

Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the
list so far on each new element.
Recall that the median of an even-numbered list is the average of
the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm
should print out:
2
1.5
2
3.5
2
2
2
"""


def sort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                c = array[i]
                array[i] = array[j]
                array[j] = c
    return array


def median(array):
    new_list = sort(array)
    if len(new_list) % 2 == 1:
        return new_list[(len(new_list) // 2)]
    else:
        return (new_list[(len(new_list) // 2) - 1] + new_list[(len(new_list) // 2)]) / 2


def main(array):
    for i in range(len(array)):
        print(median(array[0:i + 1]))


main([2, 1, 5, 7, 2, 0, 5])
