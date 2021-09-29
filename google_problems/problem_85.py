"""This problem was asked by Google.

You are given a 2D matrix of 1s and 0s where 1 represents land and 0 
represents water.

Grid cells are connected horizontally orvertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly 
one island (i.e., one or more connected land cells).

An island is a group is cells connected horizontally or vertically, 
but not diagonally. There is guaranteed to be exactly one island in this grid, 
and the island doesn't have water inside that isn't connected 
to the water around the island. Each cell has a side length of 1.

Determine the perimeter of this island.

For example, given the following matrix:

[[0, 1, 1, 0],
[1, 1, 1, 0],
[0, 1, 1, 0],
[0, 0, 1, 0]]
Return 14.
"""