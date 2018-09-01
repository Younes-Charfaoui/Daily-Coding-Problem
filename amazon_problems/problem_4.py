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
		self.max = None
		self.count = 0
		self.array = []

	def push(self , val):
		self.array.append(val)
		if val >= self.max:
			self.max = val
			

	def pop(self):
		if len(self.array) == 0:
			return None
		else:
			value = self.array.pop()
			if value = self.max:
				self.max = max(self.array)
			return value


	def max(self):
		return self.max
