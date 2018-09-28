"""This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28"""


def make_perfect(number):
    value = 10 - int(sum_number(str(number)))
    if value == 0:
        return number
    else:
        return str(number) +str(value)


def sum_number(number):
    if int(number) <= 10:
        return int(number)
    else:
        return sum_number(count(number))


def count(number):
    arr = str(number)
    r = 0
    for i in arr:
        r += int(i)
    return str(r)


print(make_perfect(22133))
