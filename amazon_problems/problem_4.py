"""This problem was asked by Amazon.
Implement a stack that has	 the following methods:
•	push(val), which pushes an element onto the stack
•	pop(), which pops off and returns the topmost element of the stack.
 If there are no elements in the stack, then it should throw an error or return null.
•	max(), which returns the maximum value in the stack currently. 
If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""


class stack(object):
    """stack object for the solution"""

    def __init__(self):
        """
        Initialize the array.

        Args:
            self: (todo): write your description
        """
        self.max = None
        self.count = 0
        self.array = []

    def push(self, val):
        """
        Push an item to the end of the list.

        Args:
            self: (todo): write your description
            val: (int): write your description
        """
        self.array.append(val)
        if val >= self.max:
            self.max = val

    def pop(self):
        """
        Remove and return the first element from the list.

        Args:
            self: (todo): write your description
        """
        if len(self.array) == 0:
            return None
        else:
            value = self.array.pop()
            if value == self.max:
                self.max = max(self.array)
            return value

    def max(self):
        """
        Returns the maximum value of the object.

        Args:
            self: (todo): write your description
        """
        return self.max
