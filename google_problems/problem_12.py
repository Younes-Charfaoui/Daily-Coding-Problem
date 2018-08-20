"""This problem was asked by Google.
The edit distance between two strings refers to the minimum 
number of character insertions, deletions, and substitutions 
required to change one string to the other. For example, 
the edit distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them."""

import math


def main(one, two):
    if len(one) > len(two):
        small = len(two)
    else:
        small = len(one)
    distance = int(math.fabs(len(one) - len(two)))
    if distance == 0:
        for i, j in zip(one, two):
            if i != j:
                distance += 1
    else:
        for i in range(small):
            if one[i] != two[i]:
                distance += 1
    return distance


print(main("kitten", "sitting"))  # should gave 3
print(main("me", "you"))  # should gave 3
print(main("majid", "younes"))  # should gave 6
print(main("hello", "ehllo"))  # should gave 2
print(main("younes", "younes"))  # should gave 2
