"""This problem was asked by Amazon.
Implement a bit array.
A bit array is a space efficient array that holds a value of 1 or 0 at each index.
•	init(size): initialize the array with size
•	set(i, val): updates index at i with val where val is either 1 or 0.
•	get(i): gets the value at index i.
"""

class BitArray:

	def __init__(self, size):
		self.data=[]
		self.size = size
		for i in range(size):
			self.data.append(0)
		
	def set(i , val):
		if 0 <= size < self.size
			self.data[i] = val

	def get(i):
		if 0 <= size < self.size
			return data[i]