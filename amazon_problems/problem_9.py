"""This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12"""

a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]

b = [[1, 2, 3],
     [4, 5, 6]]

c = [[1, 2, 3]]

d = [[1],
     [2],
     [3],
     [4],
     [5],
     [6]]

e = [[1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4]]


def main():
    matrix = e
    rs = 0
    re = len(matrix) - 1
    cs = 0
    ce = len(matrix[0]) - 1
    ci = 0
    cj = 0
    total = len(matrix) * len(matrix[0])
    now = 0
    ori = 0

    while now < total:

        if ori == 0:
            for cj in range(cs, ce + 1):
                print(matrix[ci][cj])
                now += 1
            rs += 1
            ori = 1

        elif ori == 1:
            for ci in range(rs, re + 1):
                print(matrix[ci][cj])
                now += 1
            ce -= 1
            ori = 2

        elif ori == 2:
            for cj in range(ce, cs - 1, -1):
                print(matrix[ci][cj])
                now += 1
            re -= 1
            ori = 3

        elif ori == 3:
            for ci in range(re, rs - 1, -1):
                print(matrix[ci][cj])
                now += 1
            cs += 1
            ori = 0


main()
