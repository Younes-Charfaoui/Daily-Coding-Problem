"""This problem was asked by Facebook.
Given a list of integers, return the largest product that can be made 
by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
You can assume the list has at least three integers."""

array = [-10, 10, 5, 2, -4]

positives = [x for x in array if x > 0]
negative = [x for x in array if x < 0]

positives.sort()
negative.sort()

first = positives[-1] * positives[-2] * negative[-1]
second = negative[-1] * negative[-2] * positives[-1]

if first > second:
    print(first)
else:
    print(second)
