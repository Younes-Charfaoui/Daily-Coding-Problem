"""This problem was asked by Google.

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, 
and there are coins strewn about over the map.

Given the position of all the coins and your current position, 
find the closest coin to you in terms of Manhattan distance. 
That is, you can move around up, down, left, and right, but not diagonally. 
If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o, 
and empty spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------

return (0, 4), since that coin is closest. 
This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
"""