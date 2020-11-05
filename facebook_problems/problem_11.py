"""This problem was asked by Facebook.
There is an N by M matrix of zeroes. Given N and M, write a function to count the 
number of ways of starting at the top-left corner and getting to the bottom-right corner. 
You can only move right or down.
For example, given a 2 by 2 matrix, you should return 2, since there are two ways 
to get to the bottom-right:
•	Right, then down
•	Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""


def main():
    """
    Main function.

    Args:
    """
    N = 5
    M = 5
    print(number_ways(N, M, 0, 0))


def number_ways(n, m, i, j):
    """
    Return number n i th number n at i.

    Args:
        n: (int): write your description
        m: (int): write your description
        i: (int): write your description
        j: (int): write your description
    """
    if i + 1 == n and j + 1 == m:
        return 1
    if i + 1 == n:
        return number_ways(n, m, i, j + 1)
    elif j + 1 == m:
        return number_ways(n, m, i + 1, j)
    else:
        return number_ways(n, m, i + 1, j) + number_ways(n, m, i, j + 1)


main()