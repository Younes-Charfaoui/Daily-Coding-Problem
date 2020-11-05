"""This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. 
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), 
return the second instance.
"""

class Signleton():

	def __init__(self):
     """
     Initialize the instance.

     Args:
         self: (todo): write your description
     """
		self.instance_one = None
		self.instance_two = None
		self.counter = 0

	def get_instance():
     """
     Returns the instance of the instance is_one.

     Args:
     """
		if self.counter == 0:
			self.instance_one = Signleton()
			self.instance_two = Signleton()
		self.counter += 1
		if self.counter %2 == 0:

			return self.instance_one
		else:
			return self.instance_two