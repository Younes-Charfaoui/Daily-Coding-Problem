"""This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

	- "10", a positive integer
	- "-10", a negative integer
	- "10.1", a positive real number
	- "-10.1", a negative real number
	- "1e5", a number in scientific notation
And here are examples of non-numbers:

	- "a"
	- "x 1"
	- "a -2"
	- "-"
"""

def number(data):
	first = data[0]
	real = False
	positive = True
	if first == '-':
		positive = False
	for i in data[1:]:
		if i not in [1,2,3,4,5,6,7,8,9,0]:
			return "not a number"
		if i == ".":
			real = True
	if positive :
		yield "a Positive"
	else:
		yield "a Negative"

	if real:
		return " Real Number"
	else :
		return " Integer "


