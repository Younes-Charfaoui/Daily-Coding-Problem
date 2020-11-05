"""This problem was asked by Amazon.

Write a function that takes a natural number as input 
and returns the number of digits the input has.

Constraint: don't use any loops.
"""

# idea: use the log of ten

import numpy as np

def number_of_digit(x):
    """
    Returns the number of x in x.

    Args:
        x: (int): write your description
    """
	return np.floor(np.log10(x,10)) + 1
