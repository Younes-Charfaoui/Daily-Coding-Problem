"""This problem was asked by Google.
Implement integer exponentiation. That is, implement the pow(x, y) function, 
where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.
For example, pow(2, 10) should return 1024.
"""

# naive
def pow(x,y):
    """
    Pow ( x y ) = ( x y )

    Args:
        x: (todo): write your description
        y: (todo): write your description
    """
	result = 1
	for i in range(1,y):
		result *= x
	return result

# naive 2
def pow(x,y):
    """
    Pow ( x y )

    Args:
        x: (todo): write your description
        y: (todo): write your description
    """
	return x**y

# recursive one
def power(x, y): 
    """
    Returns the power.

    Args:
        x: (todo): write your description
        y: (todo): write your description
    """
    if (y == 0): 
    	return 1
    temp = power(x, int(y / 2))
    if (int(y % 2) == 0): 
        return temp * temp         
    else: 
        return x * temp * temp